from random import randint


def generate_colour() -> tuple[int, int, int]:
    return randint(0, 255), randint(0, 255), randint(0, 255)
