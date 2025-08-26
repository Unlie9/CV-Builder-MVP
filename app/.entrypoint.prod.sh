#!/bin/sh
set -e

python backend/manage.py collectstatic --noinput

python backend/manage.py migrate --noinput

exec python -m gunicorn --chdir backend --bind 0.0.0.0:8000 --workers 3 core.wsgi:application
