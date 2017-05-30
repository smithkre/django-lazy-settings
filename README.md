Django Lazy Settings
========================

An easy way to use settings variable in django template.


How to install
--------------

You can also install it with: ``pip install django-lazy-settings``


Configuration
-------------

Add the sr app to your installed apps and define your settings :code:`SR` variable as a dictionary.

Example:

.. code-block:: python

    # settings.py
    INSTALLED_APPS = [
        ...

        'lazy_setting'
    ]


Usage examples
--------------

Use it from your template code with ``lz`` template tag:

.. code-block:: django

    {% load lazy_setting %}
    <span class="message">{% lz 'SETTING_KEY' %}</span>
    <span class="other">{% lz 'SECRET_KEY' %}</span>

