import os
import subprocess
from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

try:
    from specs import (
        BAR_BACKGROUND_COLOR,
        BAR_HEIGHT,
        BAR_POSITION,
        BORDER_WIDTH,
        BROWSER,
        COLORS,
        FOCUSED_BORDER_COLOR,
        FONT_NAME,
        FONT_SIZE,
        GROUPS,
        ICON_SIZE,
        LAUNCHER,
        MOD,
        NOTIFICATION_DAEMON,
        TERMINAL,
        TRAY_ICON_SIZE,
        UNFOCUSED_BORDER_COLOR,
        WALLPAPER,
        WIDGET_PADDING,
        WIDGET_ROUNDED,
    )
except ImportError:
    print("specs.py not found! Please create it from the example.")
    exit(1)

if not TERMINAL:
    TERMINAL = guess_terminal()

keys = [
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
    Key([MOD], "d", lazy.spawn(LAUNCHER), desc="Application launcher"),
    Key([MOD], "b", lazy.spawn(BROWSER), desc="Launch browser"),
    Key([MOD], "f", lazy.spawn("thunar"), desc="File manager"),
    Key([MOD], "s", lazy.spawn(f"{TERMINAL} -e htop"), desc="System monitor"),
    Key([MOD], "v", lazy.spawn("pavucontrol"), desc="Volume control"),
    Key([MOD], "x", lazy.spawn("nm-connection-editor"), desc="Network manager"),
    Key([MOD], "p", lazy.spawn(f"{TERMINAL} -e ranger"), desc="Ranger file manager"),
    Key([MOD], "Print", lazy.spawn("scrot"), desc="Screenshot"),
    Key([MOD, "shift"], "Print", lazy.spawn("scrot -s"), desc="Screenshot selection"),
    Key([MOD], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "h", lazy.layout.left(), desc="Move focus left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus right"),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([MOD, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([MOD, "control"], "j", lazy.layout.grow(), desc="Grow window"),
    Key([MOD, "control"], "k", lazy.layout.shrink(), desc="Shrink window"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([MOD], "m", lazy.layout.maximize(), desc="Maximize window"),
    Key([MOD], "r", lazy.restart(), desc="Restart qtile"),
    Key([MOD, "shift"], "r", lazy.reload_config(), desc="Reload qtile config"),
    Key([MOD, "shift"], "q", lazy.shutdown(), desc="Logout"),
]

groups = [Group(name) for name in GROUPS]

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

layouts = [
    layout.Columns(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
        margin_on_single=True,
    ),
    layout.Max(),
    layout.MonadTall(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        ratio=0.65,
        margin=8,
    ),
    layout.MonadWide(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        ratio=0.65,
        margin=8,
    ),
    layout.Floating(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
    ),
]

widget_defaults = dict(
    font=FONT_NAME,
    fontsize=FONT_SIZE,
    padding=WIDGET_PADDING,
    background=COLORS["bg"],
    foreground=COLORS["fg"],
)

extension_defaults = widget_defaults.copy()

def init_widgets_list() -> List[widget.base.ThreadedPollText]:
    return [
        widget.Sep(
            linewidth=0,
            padding=6,
            background=COLORS["bg"],
        ),
        widget.TextBox(
            text="",
            fontsize=ICON_SIZE,
            foreground=COLORS["purple"],
            background=COLORS["bg"],
            mouse_callbacks={"Button1": lambda: lazy.spawn(LAUNCHER)},
        ),
        widget.GroupBox(
            font=FONT_NAME,
            fontsize=ICON_SIZE,
            margin_y=3,
            margin_x=5,
            padding_y=5,
            padding_x=8,
            borderwidth=3,
            active=COLORS["fg"],
            inactive=COLORS["selected_bg"],
            rounded=WIDGET_ROUNDED,
            highlight_method="block",
            background=COLORS["bg"],
            this_current_screen_border=COLORS["purple"],
            this_screen_border=COLORS["selected_bg"],
            other_current_screen_border=COLORS["pink"],
            other_screen_border=COLORS["selected_bg"],
            urgent_alert_method="text",
            urgent_text=COLORS["red"],
            urgent_background=COLORS["bg"],
        ),
        widget.TextBox(
            text=" ",
            fontsize=ICON_SIZE,
            background=COLORS["bg"],
        ),
        widget.CurrentLayout(
            foreground=COLORS["fg"],
            background=COLORS["bg"],
        ),
        widget.TextBox(
            text="|",
            foreground=COLORS["pink"],
            background=COLORS["bg"],
            padding=5,
        ),
        widget.WindowName(
            foreground=COLORS["fg"],
            background=COLORS["bg"],
            max_chars=50,
            width=300,
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=COLORS["bg"],
        ),
        widget.TextBox(
            text=" ",
            foreground=COLORS["fg"],
            background=COLORS["bg"],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=COLORS["bg"],
        ),
        widget.Net(
            interface="wlp2s0",
            format="{down} ↓↑{up}",
            foreground=COLORS["cyan"],
            background=COLORS["bg"],
            padding=5,
        ),
        widget.TextBox(
            text=" ",
            foreground=COLORS["fg"],
            background=COLORS["bg"],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=COLORS["bg"],
        ),
        widget.ThermalSensor(
            foreground=COLORS["orange"],
            background=COLORS["bg"],
            padding=5,
            threshold=80,
            fmt="🌡{}",
        ),
        widget.TextBox(
            text=" ",
            foreground=COLORS["fg"],
            background=COLORS["bg"],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=COLORS["bg"],
        ),
        widget.Battery(
            foreground=COLORS["green"],
            background=COLORS["bg"],
            padding=5,
            format="{char} {percent:2.0%}",
            low_foreground=COLORS["red"],
            charge_char="",
            discharge_char=" ",
            empty_char=" ",
            unknown_char="?",
        ),
        widget.TextBox(
            text=" ",
            foreground=COLORS["fg"],
            background=COLORS["bg"],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=COLORS["bg"],
        ),
        widget.Volume(
            foreground=COLORS["yellow"],
            background=COLORS["bg"],
            padding=5,
            fmt="  {}",
        ),
        widget.TextBox(
            text=" ",
            foreground=COLORS["fg"],
            background=COLORS["bg"],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=COLORS["bg"],
        ),
        widget.Clock(
            format="%a %b %d  %H:%M",
            foreground=COLORS["pink"],
            background=COLORS["bg"],
        ),
        widget.TextBox(
            text=" ",
            foreground=COLORS["fg"],
            background=COLORS["bg"],
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            background=COLORS["bg"],
        ),
        widget.Systray(
            icon_size=TRAY_ICON_SIZE,
            background=COLORS["bg"],
            padding=5,
        ),
        widget.TextBox(
            text=" ",
            foreground=COLORS["fg"],
            background=COLORS["bg"],
        ),
    ]


def init_screens():
    screens = [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=BAR_HEIGHT,
                background=COLORS["bg"],
                opacity=1,
                margin=[0, 0, 0, 0],
            ),
            wallpaper=WALLPAPER if WALLPAPER else None,
            wallpaper_mode="fill" if WALLPAPER else None,
        ),
    ]
    return screens


screens = init_screens()

mouse = [
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

dgroups_key_binder = None
dgroups_app_rules = []
follow_mobile_wallpaper = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

floating_layout = layout.Floating(
    border_focus=FOCUSED_BORDER_COLOR,
    border_normal=UNFOCUSED_BORDER_COLOR,
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

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
