# -*- encoding: utf-8 -*-
import factory

from finance.models import (
    VatCode,
    VatSettings,
)


class VatSettingsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = VatSettings

    @factory.lazy_attribute
    def standard_vat_code(self):
        return VatCode.objects.get(slug=VatCode.STANDARD)
