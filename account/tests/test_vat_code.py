# -*- encoding: utf-8 -*-
import pytest

from django.core.exceptions import ValidationError
from django.test import TestCase

from account.models import VatCode


@pytest.mark.django_db
def test_vat_code():
    """Created in the migrations."""
    VatCode.objects.get(slug=VatCode.STANDARD)
