#!/usr/bin/env bash
# Build script executed by Render on every deploy.
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py compilemessages
python manage.py migrate --no-input
