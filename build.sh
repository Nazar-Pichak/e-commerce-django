#!/usr/bin/env bash
# Exit on error

python3 -m venv venv
source venv/bin/activate
# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install --upgrade pip
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations
python manage.py migrate