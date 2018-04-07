# -*- coding: utf-8 -*-
import phonenumbers
import datetime
from django import template
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from shared_foundation import constants


register = template.Library()


@register.simple_tag
def get_app_domain():
    """
    Returns the full URL to the domain. The output from this function gets
    generally appended with a path string.
    """
    url = settings.AT_APP_HTTP_PROTOCOL
    url += settings.AT_APP_HTTP_DOMAIN
    return url


@register.filter
def pretty_formatted_phonenumber(phone):
    """
    Template tag converts the "PhoneNumber" object into a "NATIONAL" format.
    See: https://github.com/daviddrysdale/python-phonenumbers
    """
    return phonenumbers.formatnumber(phone, phonenumbers.PhoneNumberFormat.NATIONAL)