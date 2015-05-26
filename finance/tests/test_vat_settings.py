# -*- encoding: utf-8 -*-
import pytest

from decimal import Decimal

from finance.models import (
    FinanceError,
    VatSettings,
)
from finance.tests.factories import VatSettingsFactory


@pytest.mark.django_db
def test_vat_settings_str():
    settings = VatSettingsFactory()
    str(settings)


@pytest.mark.django_db
def test_vat_settings_manager():
    VatSettingsFactory()
    settings = VatSettings.objects.settings()
    assert Decimal('0.20') == settings.standard_vat_code.rate


@pytest.mark.django_db
def test_vat_settings_manager_not():
    with pytest.raises(FinanceError) as excinfo:
        VatSettings.objects.settings()
    assert "VAT settings have not been set-up" in str(excinfo.value)
