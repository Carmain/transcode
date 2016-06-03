"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

from django.core.wsgi import get_wsgi_application
from worker.main import app
import os
import threading
import atexit

def monitor(app, lock_path):
    from api.models import TranscodeFile, ConvertJob

    print("Celery monitoring started...")
    state = app.events.State()

    @atexit.register
    def cleanup():
        os.remove(lock_path)

    def failed_tasks(event):
        state.event(event)
        task = state.tasks.get(event['uuid'])

        print('TASK FAILED: %s[%s] %s' % (
            task.name, task.uuid, task.info(), ))

    def sent_task(event):
      print(event)

    def received_task(event):
      print(event)

    def started_tasks(event):
      pass

    def test(event):
        print(event)

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                'task-sent': sent_task,
                'task-failed': failed_tasks,
                'task-received': received_task,
                'task-started': started_tasks
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
