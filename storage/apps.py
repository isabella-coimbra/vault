# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StorageConfig(AppConfig):
    name = 'storage'
    verbose_name = _("Swift Browser")
    app_name = True