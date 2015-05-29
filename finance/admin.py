# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import VatSettings


class VatSettingsAdmin(admin.ModelAdmin):
    pass

admin.site.register(VatSettings, VatSettingsAdmin)
