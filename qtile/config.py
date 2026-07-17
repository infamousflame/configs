from os import remove
from subprocess import Popen

from libqtile import bar, hook, layout, qtile, widget
from libqtile.backend.wayland import InputConfig
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.hook import subscribe
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras.layout.decorations import RoundedCorners
from qtile_extras.widget.decorations import GradientDecoration

from hyprlock import lock
from rofi import launcher


try:
    from specs import (
        BAR_HEIGHT,
        BAR_MARGIN,
        BORDER_RADIUS,
        BORDER_WIDTH,
        COLORS,
        COMMANDS,
        FONT_NAME,
        FONT_SIZE,
        GROUPS,
        ICON_SIZE,
        KEYS,
        MOD,
        SCREENS,
        WALLPAPER,
        WALLPAPER_SWITCH_PERIOD,
        WIDGET_PADDING,
        WIDGET_ROUNDED,
        WINDOW_MARGIN,
    )
except ImportError:
    print("specs.py not found! Please create it from the example.")
    exit(1)

if not COMMANDS.TERMINAL:
    COMMANDS.TERMINAL = guess_terminal()


@subscribe.startup_once
def startup():
    for cmd in COMMANDS.STARTUP:
        Popen(cmd)

@subscribe.unlocked
def unlock():
    remove("/dev/shm/hyprlock.conf")

@subscribe.client_managed
def set_window_opacity(win):
    win.opacity = 0.95

keys: list[Key] = [
    Key([MOD], KEYS.TERMINAL, lazy.spawn(COMMANDS.TERMINAL), desc="Launch terminal"),
    Key([MOD], KEYS.LAUNCHER, launcher(), desc="Application launcher"),
    Key([MOD], KEYS.BROWSER, lazy.spawn(COMMANDS.BROWSER), desc="Launch browser"),
    Key([MOD], KEYS.FILE_MANAGER, lazy.spawn(COMMANDS.FILE_MANAGER), desc="File manager"),
    Key([MOD], KEYS.SYSTEM_MONITOR, lazy.spawn(f"{COMMANDS.TERMINAL} -e {COMMANDS.SYSTEM_MONITOR}"), desc="System monitor"),
    Key([MOD], KEYS.KILL, lazy.window.kill(), desc="Kill focused window"),
    Key([MOD], KEYS.DOWN, lazy.layout.down(), desc="Move focus down"),
    Key([MOD], KEYS.UP, lazy.layout.up(), desc="Move focus up"),
    Key([MOD], KEYS.LEFT, lazy.layout.left(), desc="Move focus left"),
    Key([MOD], KEYS.RIGHT, lazy.layout.right(), desc="Move focus right"),
    Key([MOD, "shift"], KEYS.DOWN, lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], KEYS.UP, lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD, "shift"], KEYS.LEFT, lazy.layout.shuffle_left(), desc="Move window left"),
    Key([MOD, "shift"], KEYS.RIGHT, lazy.layout.shuffle_right(), desc="Move window right"),
    Key([MOD, "control"], KEYS.DOWN, lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, "control"], KEYS.UP, lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD, "control"], KEYS.LEFT, lazy.layout.grow_left(), desc="Grow window left"),
    Key([MOD, "control"], KEYS.RIGHT, lazy.layout.grow_right(), desc="Grow window right"),
    Key([], KEYS.BRIGHTNESS_UP, lazy.spawn(COMMANDS.BRIGHTNESS_UP, shell=True), desc="Increase brightness"),
    Key([], KEYS.BRIGHTNESS_DOWN, lazy.spawn(COMMANDS.BRIGHTNESS_DOWN, shell=True), desc="Decrease brightness"),
    Key([], KEYS.VOLUME_UP, lazy.spawn(COMMANDS.VOLUME_UP, shell=True), desc="Increase volume"),
    Key([], KEYS.VOLUME_DOWN, lazy.spawn(COMMANDS.VOLUME_DOWN, shell=True), desc="Decrease volume"),
    Key([], KEYS.MUTE, lazy.spawn(COMMANDS.MUTE, shell=True), desc="Mute volume"),
    # Key([MOD], KEYS.PASTE, lazy.spawn("cliphist list | rofi -dmenu -display-columns 2 | cliphist decode | wl-copy"), desc="Open Clipboard History"),
    Key([MOD], KEYS.CAPTURE, lazy.spawn(COMMANDS.SCREENSHOT, shell=True), desc="Take screenshot"),
    Key([MOD, "shift"], KEYS.CAPTURE, lazy.spawn(COMMANDS.SCREENSHOT_ANNOTATE, shell=True), desc="Take screenshot with annotation"),
    Key([MOD], KEYS.NORMALIZE, lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([MOD], KEYS.FLOAT, lazy.layout.floating(), desc="Toggle floating layout"),
    Key([MOD], KEYS.RESTART, lazy.restart(), desc="Restart qtile"),
    Key([MOD, "shift"], KEYS.RESTART, lazy.reload_config(), desc="Reload qtile config"),
    Key([MOD], KEYS.LOGOUT, lock(), desc="Lock screen"),
    Key([MOD, "shift"], KEYS.LOGOUT, lazy.shutdown(), desc="Logout"),
]

groups: list[Group] = [Group(name) for name in GROUPS]

for i, group in enumerate(groups):
    keys.extend(
        [
            Key(
                [MOD],
                str(i + 1),
                lazy.group[group.name].toscreen(),
                desc=f"Switch to group {i + 1}",
            ),
            Key(
                [MOD, "shift"],
                str(i + 1),
                lazy.window.togroup(group.name),
                desc=f"Move window to group {i + 1}",
            ),
        ]
    )

layouts: list[layout.Layout] = [
    layout.Plasma(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
        margin=WINDOW_MARGIN,
    ),
    layout.Columns(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
        margin=WINDOW_MARGIN,
        margin_on_single=True,
    ),
    layout.Max(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
    ),
    layout.Floating(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
    ),
    layout.Bsp(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
        margin=WINDOW_MARGIN,
    ),
    layout.Matrix(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
        margin=WINDOW_MARGIN,
    ),
    layout.MonadThreeCol(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
        margin=WINDOW_MARGIN,
    ),
    layout.Spiral(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
        margin=WINDOW_MARGIN,
    ),
    layout.TreeTab(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
        margin=WINDOW_MARGIN,
    ),
    layout.Zoomy(
        border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
        border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
        border_width=BORDER_WIDTH,
        margin=WINDOW_MARGIN,
    ),
]

NEON_GRADIENT = GradientDecoration(
    colours=[COLORS["purple"], COLORS["pink"], COLORS["cyan"], COLORS["blue"], COLORS["purple"]],
    whole_bar=True,
)

widget_defaults: dict[str, object] = dict(
    font=FONT_NAME,
    fontsize=FONT_SIZE,
    padding=WIDGET_PADDING,
    background=COLORS["bg"],
    foreground=COLORS["fg"],
)

extension_defaults: dict[str, object] = widget_defaults.copy()

def init_widgets_list() -> list[object]:
    return [
        widget.Sep(
            linewidth=0,
            padding=2,
            background=COLORS["bg"],
            decorations=[NEON_GRADIENT],
        ),
        widget.TextBox(
            text="",
            fontsize=ICON_SIZE,
            foreground=COLORS["fg"],
            background=COLORS["bg"],
            mouse_callbacks={"Button1": lambda: lazy.spawn(COMMANDS.LAUNCHER)},
            decorations=[NEON_GRADIENT],
        ),
        widget.GroupBox(
            font=FONT_NAME,
            fontsize=ICON_SIZE,
            margin_y=1,
            margin_x=2,
            padding_y=2,
            padding_x=3,
            borderwidth=2,
            active=COLORS["selected_fg"],
            inactive=COLORS["selected_bg"],
            rounded=WIDGET_ROUNDED,
            highlight_method="text",
            block_highlight_text_color=COLORS["cyan"],
            background=COLORS["bg"],
            this_current_screen_border=COLORS["cyan"],
            this_screen_border=COLORS["selected_bg"],
            other_current_screen_border=COLORS["blue"],
            other_screen_border=COLORS["selected_bg"],
            urgent_alert_method="text",
            urgent_text=COLORS["red"],
            urgent_background=COLORS["bg"],
            decorations=[NEON_GRADIENT],
        ),
        widget.CurrentLayout(
            foreground=COLORS["fg"],
            background=COLORS["bg"],
            padding=2,
            decorations=[NEON_GRADIENT],
        ),
        widget.TextBox(
            text="|",
            foreground=COLORS["pink"],
            background=COLORS["bg"],
            padding=2,
            decorations=[NEON_GRADIENT],
        ),
        widget.WindowName(
            foreground=COLORS["fg"],
            background=COLORS["bg"],
            max_chars=20,
            width=150,
            decorations=[NEON_GRADIENT],
        ),
        widget.Spacer(),
        widget.CPUGraph(
            graph_color=COLORS["green"],
            fill_color=COLORS["green"] + "33",
            background=COLORS["bg"],
            padding=3,
            decorations=[NEON_GRADIENT],
        ),
        widget.MemoryGraph(
            graph_color=COLORS["cyan"],
            fill_color=COLORS["cyan"] + "33",
            background=COLORS["bg"],
            padding=3,
            decorations=[NEON_GRADIENT],
        ),
        widget.NetGraph(
            graph_color=COLORS["orange"],
            fill_color=COLORS["orange"] + "33",
            background=COLORS["bg"],
            padding=3,
            decorations=[NEON_GRADIENT],
        ),
        widget.ThermalSensor(
            foreground=COLORS["yellow"],
            background=COLORS["bg"],
            padding=3,
            threshold=80,
            fmt="🌡{}",
            show_short_text=False,
            decorations=[NEON_GRADIENT],
        ),
        widget.Battery(
            foreground=COLORS["green"],
            background=COLORS["bg"],
            padding=3,
            format="{char} {percent:2.0%}",
            low_foreground=COLORS["red"],
            charge_char="",
            discharge_char=" ",
            empty_char=" ",
            unknown_char="?",
            show_short_text=False,
            decorations=[NEON_GRADIENT],
        ),
        widget.Volume(
            foreground=COLORS["pink"],
            background=COLORS["bg"],
            padding=3,
            fmt=" {}",
            decorations=[NEON_GRADIENT],
        ),
        widget.Clock(
            format="%a %b %d  %H:%M",
            foreground=COLORS["fg"],
            background=COLORS["bg"],
            padding=3,
            decorations=[NEON_GRADIENT],
        ),
    ]


def init_screens() -> list[Screen]:
    wallpapers: list[str] = WALLPAPER if WALLPAPER else []
    current_wallpaper_index: int = 0

    def get_current_wallpaper() -> str | None:
        if wallpapers:
            return wallpapers[current_wallpaper_index]
        return None

    def switch_wallpaper() -> None:
        qtile.call_later(WALLPAPER_SWITCH_PERIOD, switch_wallpaper)
        nonlocal current_wallpaper_index
        if wallpapers:
            current_wallpaper_index = (current_wallpaper_index + 1) % len(wallpapers)
            wallpaper = wallpapers[current_wallpaper_index]
            for screen in qtile.screens:
                screen.cmd_set_wallpaper(wallpaper, mode="fill")

    if wallpapers and WALLPAPER_SWITCH_PERIOD > 0:
        qtile.call_later(WALLPAPER_SWITCH_PERIOD, switch_wallpaper)

    screens: list[Screen] = [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=BAR_HEIGHT,
                background="#00000000",
                opacity=1,
                margin=BAR_MARGIN,
                border_width=[0, 0, 0, 0],
            ),
            wallpaper=get_current_wallpaper(),
            wallpaper_mode="fill" if wallpapers else None,
        ) for _ in range(SCREENS)
    ]
    return screens


screens: list[Screen] = init_screens()

mouse: list[Click | Drag] = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder: str | None = None
dgroups_app_rules: list[object] = []
follow_mobile_wallpaper: bool = True
bring_front_click: bool = False
floats_kept_above: bool = True
cursor_warp: bool = False

floating_layout: layout.Floating = layout.Floating(
    border_focus=RoundedCorners(colour=COLORS["focused_border"], radius=BORDER_RADIUS),
    border_normal=RoundedCorners(colour=COLORS["unfocused_border"], radius=BORDER_RADIUS),
    border_width=BORDER_WIDTH,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="lxpolkit"),
        Match(wm_class="nm-connection-editor"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="galculator"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="gnome-calculator"),
        Match(wm_class="qemu"),
        Match(wm_class="Steam"),
        Match(wm_class="steam"),
        Match(wm_class="steamwebhelper"),
        Match(wm_class="org.wezfurlong.wezterm"),
        Match(wm_type="dialog"),
        Match(wm_type="menu"),
        Match(wm_type="notification"),
        Match(wm_type="splash"),
        Match(wm_type="toolbar"),
    ],
)

auto_fullscreen: bool = True
focus_on_window_activation: str = "smart"
reconfigure_screens: bool = True
auto_minimize: bool = True
wl_xcursor_theme: str | None = None
wl_xcursor_size: int = 24
wl_input_rules: dict[str, InputConfig] = {
    "type:touchpad": InputConfig(tap=True, natural_scroll=False),
}
