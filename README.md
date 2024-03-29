
# django-htmx-fun

A small Django application to advertise the fun [htmx](//htmx.org) can bring you.

It implements a Single-Page-Application for writing a diary.

The entries in the diary database get lazy loaded (endless scrolling) via [hx-trigger="revealed"](https://htmx.org/attributes/hx-trigger/)

# Why I love htmx?

If you look into the past then one thing is clear: stateless has won. Nobody starts a new project with [Corba](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture)
these days. Stateless http is the winner.

I don't understand why JavaScript based frontend frameworks seem to be the only way for new projects.

I want the client/browser to be SSS (simple, stupid and stateless).

I need to validate my data on the server anyway. So why should I validate them on the client?

The Django Forms library has all you need to write database focused applications.

Sending HTML fragments over the wire keeps my application simple.

There is just one thing which is outdated (although it is still perfectly fine). The need
for a full page refresh after submitting a form.

I want html pages with several small forms and I want to load and submit each of them 
individually. This does not mean I want to write a Single-Page-Application. There
are more colors than black and white. 

For more about htmx see the homepage: [htmx.org](//htmx.org)

[HTMX: Frontend Revolution (Slides from DjangoCon 2021)](https://docs.google.com/presentation/d/12dgaBnUgl4cmEkiOhUJL5hsbGQ6hB5sslDuozmBjVUA/edit?usp=sharing)

Youtube video of the Talk [DjangoCon US 2021: HTMX, Frontend Revolution](https://www.youtube.com/watch?v=z0yPTv15Fjk)

## Install

If you want to install my small htmx demo application:

```
python3 -m venv django-htmx-fun-env
cd django-htmx-fun-env
. bin/activate
pip install -e git+https://github.com/guettli/django-htmx-fun.git#egg=django-htmx-fun
```

The source code is now in src/django-htmx-fun/

## Run Database Migrations

```
manage.py migrate
```

## Start Webserver
```
manage.py runserver
```

Diary: http://127.0.0.1:8000/

## Admin
```
manage.py createsuperuser

```
Admin: http://127.0.0.1:8000/admin

## No need for the POST/Redirect/GET pattern

If you are used to django's form handling, then you are used to the [POST/Redirect/GET Pattern](https://en.wikipedia.org/wiki/Post/Redirect/Get). This means after the client submitted a valid form, the server response has the http status 302 with a new location URL.

This is not needed if you submit a form via htmx and you just want to update one part of the whole page.

I use this pattern now:

Case 1: The http POST was successful, and data was changed. The server returns the status code 201 "Created". I use this even if data was changed, and not "created". I use this and not the usual 200 to simplify testing. I never ever want to confuse the http status of a successful htmx POST with the http status of an invalid traditional django http POST. The response contains the new HTML. No need for a redirect.

Case 2: The http POST was not successful, since the data in the form was not valid. Then my server code returns 422. 

Related question: [Which http status codes to use when processing http post?](https://stackoverflow.com/q/69773241/633961)

## Full Page (aka "client-side") Redirect

If you use htmx, then most http responses will contains html fragments which will get swapped into the current page.

But sometimes you want to do a traditional full page redirect. In the htmx docs it is called "client-side" redirect.

Then you need return a http response which has the http header "HX-Redirect" set to the URL of the new location. Docs: [Response Headers](https://htmx.org/docs/#response-headers)

A common mistake is the set the status code if this response to 302. But this will trigger a redirect inside htmx.

Here is some code to do a full page redirect with Django: [hx-target: swap html vs full page reload](https://stackoverflow.com/a/65569741/633961)

## Naming Pattern

Here is my personal naming pattern, which helps me to read the source more easily

**_page():** 

Function based view. 

`foo_page(request, ...)`. 

Returns a HttpResponse with a full page. 

URL: `/foo`

This servers only http GET. Updates (http POST) go to _hxpost URLs.

---

**_hx():**

Function based view.

`foo_hx(request, ...)`

This method should be called via HTTP-GET. Returns a HttpResponse which only contains a HTML fragment. 

URL: `/foo_hx`

---

**_hxpost():**

Function based view.

`foo_hxpost(request, ...)`

This methods should be called via HTTP-POST. Returns a HttpResponse which only 
contains a HTML fragment. 

URL: `/foo_hxpost`

It makes sense to use the [require_POST decorator](https://docs.djangoproject.com/en/dev/topics/http/decorators/#django.views.decorators.http.require_POST),if you have concerns that a GET request (where request.POST is empty) could accidently change data.

---

**_json():**

Function based view.

`foo_json(request, ...)`

This method returns a [JSONResponse](https://docs.djangoproject.com/en/dev/ref/request-response/#jsonresponse-objects).

URL: `/foo_json`

TODO: I am not happy with this yet, since you can't distinguish between a method
which returns a JSON data (dictionary), JSON string or JSONResponse.

---

**_html():**

Python method which returns a HTML SafeString. 

Usually created via [format_html()](https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.html.format_html).

## Flat URL Namespace

Above naming pattern makes it very use to get to the corresponding code. 

Imagine you get a message from tool monitoring your servers. There is an exception at URL "/sunshine/123",
then I know the name of the method which handles this URL. The method is "sunshine_page()".

If you need several pages for a model, then you will not use "/sunshine/foo" and "/sunshine/bar", but instead "/sunshine_foo" and "/sunshine_bar".

## Opinionated Best Practices

I switched from Django class-based-views (CBV) to function-based-views (FBV). This simplifies things. 
One URL corresponds to one Python method. If an action requires two HTTP verbs (GET and POST), then I use **two URLs**. Posts
always go to hx-methods, not to URLs returning full pages.

I like it conditionless. I try to avoid to have too many "if" and "else".

I avoid to use `if request.method == 'POST'`. This means I don't handle different http verbs in one function based view. A function based view handles either GET xor a POST. URLs are cheap I create two URLs if I need a a readonly view and a view which does something.

I only use the http verbs GET and POST, although htmx can do http PUT, http PATCH, http DELETE, ...

I don't use the special http headers which get added by htmx. I avoid this (pseudo code): "if request is a htmx request, then ...".
Instead I create two endpoints: One which returns a full page, one which returns a fragment.

Goodbye formsets. I use several `<form>` tags in one page. This means I hardly use formsets. Some for the "prefix" of forms: Since
I don't put several Django form instances into one `<form>` tag, I don't need the prefix any more.


## Screenshot

![diary-django-htmx](docs/diary-django-htmx.png)

In devtools you can see the lazy loading of the endless scrolling

... All this is possible without writing a single line of JavaScript :-)


## Pull Requests are welcome

You have an idea how to improve this example? Great! Just do it, provide a pull request and I will merge it.

## Related

* [Güttli Django Tips](https://github.com/guettli/django-tips)
* [Güttli's opinionated Python Tips](https://github.com/guettli/python-tips)
* [Güttli working-out-loud](https://github.com/guettli/wol)
* [Güttli's Programming Guidelines (long)](https://github.com/guettli/programming-guidelines)

