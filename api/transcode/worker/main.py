from os import path
from converter import Converter
from converter.ffmpeg import FFMpeg
from celery import Celery
from celery.utils.log import get_task_logger
import subprocess

logger = get_task_logger(__name__)


app = Celery('tasks', backend="amqp", broker="amqp://guest@localhost//")
app.conf.CELERY_SEND_EVENTS = True
app.conf.CELERY_SEND_TASK_SENT_EVENT = True


@app.task(name="split")
def split(filePath):
    c = Converter()
    infos = c.probe(filePath)
    duration = infos.streams[0].duration
    remainingTime = duration
    part_duration = min(300, remainingTime)
    dirPath = path.dirname(filePath)
    splitted_path = path.splitext(path.basename(filePath))
    ext = splitted_path[1]
    baseName = splitted_path[0]

    part_id = 0
    parts = []

    while True:
        output_name = "{}.part_{}{}".format(baseName, part_id, ext)
        output_path = path.join(dirPath, output_name)
        timestamp = duration - remainingTime
        print(filePath)
        print(output_path)
        subprocess.call([
            "ffmpeg",
            "-i",
            filePath,
            "-t",
            str(part_duration),
            "-ss",
            str(timestamp),
            "-c",
            "copy",
            output_path
        ])

        remainingTime -= part_duration
        part_duration = min(part_duration, remainingTime)
        part_id += 1
        parts.append(output_path)
        if remainingTime == 0:
            break


    return parts


@app.task(name="convert")
def convert(filePath, fileUUID, dest_type=('mkv', 'h264'), audio_only=False):
    parts = split(filePath)
    dirPath = path.dirname(filePath)
    baseName = path.splitext(path.basename(filePath))[0]
    output_name = "{}.{}".format(baseName, dest_type[0])
    output_path = path.join(dirPath, output_name)


    parts_file_path = path.join(dirPath, "{}.{}".format(baseName, "txt"))
    parts_file = open(parts_file_path, "w")

    for part in parts:
        convert_part(part, dest_type, audio_only)
        parts_file.write("file '{}'\n".format(part))

    parts_file.close()

    concatenate(parts_file_path, output_path)


@app.task(name="convert_part")
def convert_part(filePath, dest_type=('mkv', 'h264'), audio_only=False):
  c = Converter()
  infos = c.probe(filePath)
  if audio_only:
    convert_options = {
      'format': 'mp3',
      'audio': {
        'codec': "mp3"
      }
    }
  else:
    convert_options = {
      'format': dest_type[0],
      'audio': {
        'codec': infos.audio.codec,
        'samplerate': infos.audio.audio_samplerate,
        'channels': infos.audio.audio_channels
      },
      'video': {
        'codec': dest_type[1],
        'width': infos.video.video_width,
        'height': infos.video.video_height,
        'fps': infos.video.video_fps
      },
      'subtitle': {
        'codec': 'copy'
      }
    }
  dirPath = path.dirname(filePath)
  baseName = path.splitext(path.basename(filePath))[0]
  newFileName = "{}.{}".format(baseName, convert_options.get("format"))
  outputPath = path.join(dirPath, newFileName)

  logger.info(convert_options)

  conv = c.convert(filePath, outputPath, convert_options, timeout=None)

  for timecode in conv:
    pass


@app.task(name="concatenate")
def concatenate(parts_file, destination_path):
    c = Converter()

    subprocess.call([
        "ffmpeg",
        "-f",
        "concat",
        "-i",
        parts_file,
        "-c",
        "copy",
        destination_path
    ])
