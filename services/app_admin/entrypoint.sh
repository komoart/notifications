#!/bin/bash

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$DB_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up"

python3 manage.py migrate
python3 manage.py collectstatic --no-input
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='notification_admin').exists() or User.objects.create_superuser('notification_admin', 'notification_admin@admin.local', '^Z0t&Upo&8&8')"
python3 manage.py loaddata fixtures/admin_panel_data.json

gunicorn -c gunicorn.conf.py config.wsgi:application
