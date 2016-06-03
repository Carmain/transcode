#! /bin/sh

celery -A main worker --loglevel=info --autoreload
