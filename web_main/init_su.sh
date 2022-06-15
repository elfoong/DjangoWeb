#!/bin/sh

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('psh0718', 'admin@myapp.local', 'psh0718')" | python manage.py shell
