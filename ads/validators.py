from django.core.exceptions import ValidationError


def check_not_true(value: bool):
    """проверка на требуемое значение False, если True вызовет ValidationError"""
    if value:
        raise ValidationError(f'can not be True')


