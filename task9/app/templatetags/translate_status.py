from django import template
from app.const.models import UserStatuses

register = template.Library()


@register.filter
def translate_status(value):
    for item in list(UserStatuses):
        if value == item:
            return item.name

    return value

