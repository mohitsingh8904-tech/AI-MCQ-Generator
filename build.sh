#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py migrate

python manage.py shell <<EOF
from django.contrib.auth.models import User

username = "admin"
email = "admin@example.com"
password = "Admin@12345"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created")
else:
    print("Superuser already exists")
EOF

python manage.py collectstatic --noinput