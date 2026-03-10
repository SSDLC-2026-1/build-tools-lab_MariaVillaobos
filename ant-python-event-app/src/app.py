import re

VALID_TICKETS = {"general", "vip", "student"}

def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None

def is_valid_registration_code(code: str) -> bool:
    """Validate registration code format: EV- followed by exactly 4 digits"""
    if not code or not isinstance(code, str):
        return False
    pattern = r"^EV-\d{4}$"
    return re.match(pattern, code) is not None

def validate_attendee(attendee: dict) -> list:
    errors = []

    if not attendee.get("name") or not attendee["name"].strip():
        errors.append("Invalid name")

    if not is_valid_email(attendee.get("email", "")):
        errors.append("Invalid email")

    age = attendee.get("age")
    if not isinstance(age, int) or age < 18:
        errors.append("Attendee must be 18 or older")

    if attendee.get("ticket_type") not in VALID_TICKETS:
        errors.append("Invalid ticket type")
    
    # New validation for registration code
    reg_code = attendee.get("registration_code")
    if reg_code is not None:  # Only validate if provided
        if not is_valid_registration_code(reg_code):
            errors.append("Invalid registration code format (must be EV- followed by 4 digits)")

    return errors
