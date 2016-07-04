from django import template

register=template.Library()

@register.filter
def custom_brackets(value):
    if value!="":
        return '({})'.format(value)
    else:
        return value
