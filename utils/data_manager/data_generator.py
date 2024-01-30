from random import randint


def generate_random_phone_valid():
    phone = "9" + str(randint(11111111, 99999999))
    return phone
