Django Lazy Settings
========================

An easy way to use settings variable in django template.


How to install
--------------

You can also install it with: ``pip install django-lazy-settings``


Configuration
-------------

Add the lazy_setting app to your installed apps.

Example:

```python

    # settings.py
    INSTALLED_APPS = [
        ...

        'lazy_setting'
    ]
```

Usage examples
--------------

Use it from your template code with ``lz`` template tag:

```django
    {% load lazy_setting %}
    <span class="message">{% lz 'SETTING_KEY' %}</span>
    <span class="other">{% lz 'SECRET_KEY' %}</span>
```
