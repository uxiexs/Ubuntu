#!/user/bin/env python3
# coding: utf-8

from django.conf import settings as origian_settings


def settings(request):
    return {'settings': origian_settings}


def ip_address(request):
    return {'ip_address': request.META['REMOTE_ADDR']}
