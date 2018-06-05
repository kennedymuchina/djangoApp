web: python manage.py runserver 0.0.0.0:5000
web: sh -c 'cd ./portfolioApp/'

web: gunicorn portfolioApp.wsgi --log-file -
