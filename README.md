# django-clear-cache


![I don't always clear my cache...](https://github.com/rdegges/django-clear-cache/raw/master/clear_cache.jpg)


I often find myself in situations where I need to fully clear my website's
cache (memcached or whatever). Often times this is required because:

- I'm deploying new code and it will fail to run properly with my currently
  cached objects.
- I need to purge invalid (or old) information.
- A *million* other reasons.

The standard way to clear your cache is to open up a management shell, eg:

``` bash
$ python manage.py shell
Python 2.7.3 (default, Apr 20 2012, 22:39:59) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.cache import cache
>>> cache.clear()
```

But obviously, this is annoying as I have to manually log into my production
shell.

``django-clear-cache`` makes this process as easy as running a single
management command.


## Install

To install ``django-clear-cache``, simply run ``pip install django-clear-cache``
and you'll get the latest version installed automatically.

Next, modify your Django ``settings.py`` file, and add ``clear_cache`` to your
``INSTALLED_APPS`` setting:

``` python
INSTALLED_APPS = (
    # ...
    'clear_cache',
)
```

## Usage

To clear your cache, simply run the ``clear_cache`` management command:

``` bash
$ python manage.py clear_cache
Your cache has been cleared!
```

**NOTE**: This will only (obviously) work if you've got a cache configured (eg:
memcached, local memory, etc.). If you have no idea what I'm talking about,
read through the [official Django caching docs](https://docs.djangoproject.com/en/dev/topics/cache/?from=olddocs).


## TODO

- Write unit tests.
