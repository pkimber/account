# -*- encoding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models

from reversion import revisions as reversion

from base.model_utils import TimeStampedModel
from base.singleton import SingletonModel


def default_vat_code():
    return VatCode.objects.get(slug=VatCode.STANDARD).pk


def legacy_vat_code():
    """For records which were created before we introduced VAT codes."""
    return VatCode.objects.get(slug=VatCode.LEGACY).pk


class FinanceError(Exception):

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr('%s, %s' % (self.__class__.__name__, self.value))


class VatCodeManager(models.Manager):

    def exempt(self):
        return self.model.objects.get(slug=self.model.EXEMPT)


class VatCode(TimeStampedModel):
    """VAT code and rates.

    https://www.gov.uk/rates-of-vat-on-different-goods-and-services

    VAT rates for goods and services
    Rate            % of VAT    What the rate applies to
    Standard        20%         Most goods and services
    Reduced rate    5%          Some goods and services, eg home energy
    Zero rate       0%          Zero-rated goods and services, eg most food

    https://www.gov.uk/rates-of-vat-on-different-goods-and-services

    No VAT is charged on goods or services that are:

    - exempt from VAT
    - outside the scope of the UK VAT system

    """

    EXEMPT  = 'E'
    LEGACY  = 'L'
    STANDARD  = 'S'

    slug = models.SlugField(max_length=10)
    description = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=3)
    deleted = models.BooleanField(default=False)
    objects = VatCodeManager()

    class Meta:
        verbose_name = 'VAT code'

    def __str__(self):
        return "code: {}, rate: {}".format(
            self.slug,
            self.rate,
        )

reversion.register(VatCode)


class VatSettingsManager(models.Manager):

    def settings(self):
        try:
            return self.model.objects.get()
        except self.model.DoesNotExist:
            raise FinanceError(
                "VAT settings have not been set-up in admin"
            )


class VatSettings(SingletonModel):

    standard_vat_code = models.ForeignKey(
        VatCode,
        default=default_vat_code,
        related_name='+'
    )
    vat_number = models.CharField(max_length=12, blank=True)
    objects = VatSettingsManager()

    class Meta:
        verbose_name = 'VAT settings'

    def __str__(self):
        return "Standard: {}, VAT Number: {}".format(
            self.standard_vat_code.rate,
            self.vat_number,
        )

reversion.register(VatSettings)
