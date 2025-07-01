import phonenumbers
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    try:
        z = phonenumbers.parse(value,None)
        if not phonenumbers.is_valid_number(z):
            raise ValidationError("Invalid phone number.")
    except phonenumbers.NumberParseException:
        raise ValidationError("Invalid phone number format.")