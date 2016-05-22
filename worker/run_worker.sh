#! /bin/sh

celery -A main worker --loglevel=info --config=settings
