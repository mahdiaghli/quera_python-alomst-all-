import re

def validate_phone(number):
    return re.match(r"^09[0-9]{9}$", number) or re.match(r"^\+989[0-9]{9}$", number) or re.match(r"^00989[0-9]{9}$",
                                                                                                 number)


def validate_email(email):
    return re.match(r"^[a-zA-Z1-9\.\_]+@[a-zA-Z1-9]+\.[a-zA-Z]{3}$", email)
