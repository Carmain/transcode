## Worker configuration

BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'db+sqlite:///results.db'

CELERY_IMPORTS = ('main')

CELERY_ACCEPT_CONTENT = ['json']
