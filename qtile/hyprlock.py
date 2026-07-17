from enum import StrEnum
from random import randint

from libqtile.lazy import lazy

from colour import generate_colour
from specs import COMMANDS

class TextColour(StrEnum):
    LIGHT: str = "rgba(255, 255, 255, 0.8)"
    DARK: str = "rgba(0, 0, 0, 0.8)"
    COMPLEMENT_LIGHT: str = "rgba(255, 255, 255, 0.4)"
    COMPLEMENT_DARK: str = "rgba(0, 0, 0, 0.4)"

@lazy.function
def lock(qtile):
    colour: tuple[int, int, int] = generate_colour()
    bg_colour: str = f"rgba({",".join(map(str, colour))}, 1.0)"
    text_colour: str
    complement_colour: str
    text_colour, complement_colour = (
        (TextColour.LIGHT, TextColour.COMPLEMENT_DARK)
        if sum(colour) < 383 else
        (TextColour.DARK, TextColour.COMPLEMENT_LIGHT)
    )
    with open("/dev/shm/hyprlock.conf", "w") as f:
        f.write(CONFIG.format(
            bg_colour=bg_colour,
            text_colour=text_colour,
            complement_colour=complement_colour,
        ))
    qtile.spawn(COMMANDS.LOCK)

CONFIG = """# General Settings
general {{
    disable_loading_bar = false
    hide_cursor = true
    grace = 0 # No grace period (locks immediately)
    no_fade_in = false
}}

# Background: Plain for now
background {{
    monitor =
    color = {bg_colour}
    blur_passes = 0
    contrast = 1.0
    brightness = 1.0
    vibrancy = 0.0
    vibrancy_darkness = 0.0
}}

# Label: Digital Clock
label {{
    monitor =
    text = cmd[update:1000] echo "$(date +'%H:%M:%S')"
    color = {text_colour}
    font_size = 80
    font_family = Sans
    position = 0, -50
    halign = center
    valign = center
}}

# Label: Date
label {{
    monitor =
    text = cmd[update:1000] echo "$(date +'%A, %B %d')"
    color = {text_colour}
    font_size = 20
    font_family = Sans
    position = 0, 100
    halign = center
    valign = center
}}

# Input Field: Password Box
input-field {{
    monitor =
    size = 250, 50
    outline_thickness = 2
    dots_size = 0.25
    dots_spacing = 0.2
    dots_center = true
    outer_color = {text_colour}
    inner_color = {complement_colour}
    font_color = {text_colour}
    fade_on_empty = true
    placeholder_text = <i>Password...</i>
    hide_input = false
    position = 0, 200
    halign = center
    valign = center
    rounding = 10
}}
"""
