import re

from django.core.exceptions import ValidationError


def check_email_blacklist(value: str):
    """Если email домена rambler.ru вызовет ValidationError"""
    if re.fullmatch(r'\w+@rambler\.ru', value):
        raise ValidationError(f"can not be @rambler.ru")
