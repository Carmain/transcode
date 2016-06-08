from os import path
from converter import Converter
from celery import Celery

app = Celery('tasks', backend="amqp", broker="amqp://guest@localhost//")
app.conf.CELERY_SEND_EVENTS = True
app.conf.CELERY_SEND_TASK_SENT_EVENT = True


@app.task(name="convert")
def convert(filePath, fileUUID, dest_type=('mkv', 'h264')):
  c = Converter()
  infos = c.probe(filePath)
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

  conv = c.convert(filePath, outputPath, convert_options)

  for timecode in conv:
    pass
