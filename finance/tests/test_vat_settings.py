# -*- encoding: utf-8 -*-
import pytest

from finance.models import VatSettings
from finance.tests.factories import VatSettingsFactory


@pytest.mark.django_db
def test_vat_settings_str():
    settings = VatSettingsFactory()
    str(settings)
