# -*- encoding: utf-8 -*-
import pytest

from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase

from finance.models import VatCode


@pytest.mark.django_db
def test_vat_code():
    """Created in the migrations."""
    VatCode.objects.get(slug=VatCode.STANDARD)


@pytest.mark.django_db
def test_vat_code_exempt():
    vat_code = VatCode.objects.exempt()
    assert Decimal() == vat_code.rate
