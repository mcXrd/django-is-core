from __future__ import unicode_literals

from django import template

register = template.Library()


@register.filter()
def split(value):
    return value.split(' ')
