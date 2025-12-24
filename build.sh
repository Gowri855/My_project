#!/usr/bin/env bash
# exit on error
set -o errexit


echo "Installing dependencies..."
pip install -r requirements.txt


echo "Collecting static files..."
python manage.py collectstatic --no-input


echo "Creating migrations..."
python manage.py makemigrations


echo "Running migrations..."
python manage.py migrate


echo "Build completed successfully!"
python manage.py load_production_data

# Existing lines (example)
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# TEMP: create superuser on Render if none exists
python manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); U.objects.filter(is_superuser=True).exists() or U.objects.create_superuser('gowri855','whoops855@gmail.com','AjaiGowriAlohomora@855')"
