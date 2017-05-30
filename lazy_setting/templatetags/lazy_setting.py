from django import template

register = template.Library()

from django.conf import settings

@register.simple_tag(name='lz')
def read_setting(key):
    try:
        return getattr(settings, key)
    except: 
        return None
