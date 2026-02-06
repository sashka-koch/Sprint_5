import random
import string

def generate_email(first_name="aleksandra", last_name="kochenkova", cohort="44", domain="yandex.com"):
    random_number = random.randint(100, 999)
    email = f"{first_name}_{last_name}_{cohort}_{random_number}@{domain}"
    return email


def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
