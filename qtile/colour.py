from colorsys import hsv_to_rgb
from datetime import datetime
# from random import randint


# def generate_colour() -> tuple[int, int, int]:
#     return randint(0, 255), randint(0, 255), randint(0, 255)


def generate_colour() -> tuple[int, int, int]:
    """Generate a colour based on the tine of the hour."""
    minute: int = datetime.now().minute
    second: int = datetime.now().second
    hue: float = (minute * 60 + second) / 3600.0
    rgb: tuple[int, int, int] = tuple(round(x * 255) for x in hsv_to_rgb(hue, 1.0, 1.0))
    return rgb
