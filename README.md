# django-htmx-fun

A small Django application to advertise the fun [htmx](//htmx.org) can bring you.

It implements a Single-Page-Application for writing a diary.

The entries in the diary database get lazy loaded (endless scrolling) via [hx-trigger="revealed"](https://htmx.org/attributes/hx-trigger/)

# Why I love htmx?

If you look into the past then one thing is clear: stateless has won. Nobody starts a new project with [Corba](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture)
these days. Stateless http is the winner.

I don't understand why JavaScript based frontend frameworks seem to be the only way for new projects.

I need to validate my data on the server anyway. So why should I validate them on the client?

The Django Forms library has all you need to write database focused applications.

Sending HTML fragements over the wire keeps my application simple.

There is just one thing which is outdated (although it is still perfectly fine): 
[Post/Redirect/Get Pattern](https://en.wikipedia.org/wiki/Post/Redirect/Get)

I want one html page with several small forms and I want to load and submit each of them 
individually. This does not mean I want to write a Single-Page-Application. There
are more colors than black and white. 


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

