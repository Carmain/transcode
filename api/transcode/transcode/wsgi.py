"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application
from worker.main import app
import os
import threading
import atexit
import ast
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

def monitor(app, lock_path):
    from api.models import TranscodeFile, ConvertJob, ConvertedFile

    print("Celery monitoring started...")
    state = app.events.State()

    @atexit.register
    def cleanup():
        os.remove(lock_path)

    def failed_task(event):
        state.event(event)
        task = state.tasks.get(event['uuid'])

        print('TASK FAILED: %s[%s] %s' % (
            task.name, task.uuid, task.info(), ))

    def received_task(event):
      kwargs_dict = ast.literal_eval(event.get('kwargs'))
      file_uuid = kwargs_dict.get("fileUUID")
      tr_file = TranscodeFile.objects.get(uuid=file_uuid)
      ConvertJob.objects.create(file=tr_file, task_uuid=event.get("uuid"))

    def started_task(event):
      convert_job = ConvertJob.objects.get(task_uuid=event.get("uuid"))
      convert_job.state = 2
      convert_job.save()

    def succeeded_task(event):
      convert_job = ConvertJob.objects.get(task_uuid=event.get("uuid"))
      tr_file = convert_job.file
      cv_file = ConvertedFile.objects.create(fileType="mkv", transcode_file=tr_file)
      print("ConvertJob succeeded")


    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
            'task-failed': failed_task,
            'task-received': received_task,
            'task-started': started_task,
            'task-succeeded': succeeded_task
        })
        recv.capture(limit=None, timeout=None, wakeup=True)

lock_path = os.path.join(os.path.dirname(__file__), "monitor.lock")

try:
  # Create a lock file to prevent opening of multiple threads
  os.open(lock_path, os.O_CREAT|os.O_EXCL)

  thread = threading.Thread(target=monitor, args=(app, lock_path))
  thread.daemon = True
  thread.start()
except FileExistsError:
  pass

application = get_wsgi_application()
