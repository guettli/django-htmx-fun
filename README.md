# django-htmx-fun
A small Django application to advertise the fun [htmx](//htmx.org) can bring you 

## Install

```
python3 -m venv django-htmx-fun-env
cd django-htmx-fun-env
. bin/activate
pip install -e git+ssh://git@github.com/guettli/django-htmx-fun.git#egg=django_htmx_fun
```

## Run Database Migrations

```
manage.py migrate
```

## Start Webserver
```
manage.py runserver
 ...
 Starting development server at http://127.0.0.1:8000/
```

## Things to improve

If a hx-reponse fails, for example there is a typo in the code and the django-debug view gets returned, then you see nothing.
You can open devtools and there you find the error. But a more convenient way would be handy.

