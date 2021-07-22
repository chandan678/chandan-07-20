npm install -g @vue/cli

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
exec "$@"