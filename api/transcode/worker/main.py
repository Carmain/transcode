from os import path
from converter import Converter
from celery import Celery

app = Celery('tasks', backend="amqp", broker="amqp://guest@localhost//")
app.conf.CELERY_SEND_EVENTS = True
app.conf.CELERY_SEND_TASK_SENT_EVENT = True


@app.task(name="convert")
def convert(filePath, fileUUID):
  convert_options = {
    'format': 'mkv',
    'audio': {
      'codec': 'mp3',
      'samplerate': 11025,
      'channels': 2
    },
    'video': {
      'codec': 'h264',
      'width': 720,
      'height': 400,
      'fps': 15
    },
    'subtitle': {
      'codec': 'copy'
    },
    'map': 0
  }
  c = Converter()
  dirPath = path.dirname(filePath)
  baseName = path.splitext(path.basename(filePath))[0]
  newFileName = "{}.{}".format(baseName, convert_options.get("format"))
  outputPath = path.join(dirPath, newFileName)

  conv = c.convert(filePath, outputPath, convert_options)

  for timecode in conv:
    pass
