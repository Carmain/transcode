from celery import Celery

app = Celery('tasks')

@app.task
def convert(path, format):
  return path
