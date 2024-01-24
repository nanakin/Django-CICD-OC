#!/bin/sh
poetry run python manage.py migrate
poetry run python manage.py collectstatic --no-input
poetry run gunicorn -w 2 -b :8000 oc_lettings_site.wsgi