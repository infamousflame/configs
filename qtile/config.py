from libqtile import bar, hook, layout, qtile, widget
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
        K,
        LAUNCHER,
        LOCK_COMMAND,
        MOD,
        NET_INTERFACE,
        NOTIFICATION_DAEMON,
        SCREENS,
        SYSTEM_MONITOR,
        TERMINAL,
        TRAY_ICON_SIZE,
        UNFOCUSED_BORDER_COLOR,
        WALLPAPER,
        WALLPAPER_SWITCH_PERIOD,
        WIDGET_PADDING,
        WIDGET_ROUNDED,
    )
except ImportError:
    print("specs.py not found! Please create it from the example.")
    exit(1)

if not TERMINAL:
    TERMINAL = guess_terminal()

keys: list[Key] = [
    Key([MOD], K.TERMINAL, lazy.spawn(TERMINAL), desc="Launch terminal"),
    Key([MOD], K.LAUNCHER, lazy.spawn(LAUNCHER), desc="Application launcher"),
    Key([MOD], K.BROWSER, lazy.spawn(BROWSER), desc="Launch browser"),
    Key([MOD], K.FILE_MANAGER, lazy.spawn("thunar"), desc="File manager"),
    Key([MOD], K.SYSTEM_MONITOR, lazy.spawn(f"{TERMINAL} -e {SYSTEM_MONITOR}"), desc="System monitor"),
    Key([MOD], K.KILL, lazy.window.kill(), desc="Kill focused window"),
    Key([MOD], K.DOWN, lazy.layout.down(), desc="Move focus down"),
    Key([MOD], K.UP, lazy.layout.up(), desc="Move focus up"),
    Key([MOD], K.LEFT, lazy.layout.left(), desc="Move focus left"),
    Key([MOD], K.RIGHT, lazy.layout.right(), desc="Move focus right"),
    Key([MOD, "shift"], K.DOWN, lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], K.UP, lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD, "shift"], K.LEFT, lazy.layout.shuffle_left(), desc="Move window left"),
    Key([MOD, "shift"], K.RIGHT, lazy.layout.shuffle_right(), desc="Move window right"),
    Key([MOD, "control"], K.DOWN, lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, "control"], K.UP, lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD, "control"], K.LEFT, lazy.layout.grow_left(), desc="Grow window left"),
    Key([MOD, "control"], K.RIGHT, lazy.layout.grow_right(), desc="Grow window right"),
    Key([MOD], K.NORMALIZE, lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([MOD], K.FLOAT, lazy.layout.floating(), desc="Toggle floating layout"),
    Key([MOD], K.RESTART, lazy.restart(), desc="Restart qtile"),
    Key([MOD, "shift"], K.RESTART, lazy.reload_config(), desc="Reload qtile config"),
    Key([MOD], K.LOGOUT, lazy.spawn(LOCK_COMMAND), desc="Lock screen"),
    Key([MOD, "shift"], K.LOGOUT, lazy.shutdown(), desc="Logout"),
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
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
    ),
    layout.Columns(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
        margin_on_single=True,
    ),
    layout.Max(),
    layout.Floating(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
    ),
    layout.Bsp(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
    ),
    layout.Matrix(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
    ),
    layout.MonadThreeCol(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
    ),
    layout.Spiral(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
    ),
    layout.TreeTab(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
    ),
    layout.Zoomy(
        border_focus=FOCUSED_BORDER_COLOR,
        border_normal=UNFOCUSED_BORDER_COLOR,
        border_width=BORDER_WIDTH,
        margin=8,
    ),
]

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
            margin_y=1,
            margin_x=2,
            padding_y=2,
            padding_x=3,
            borderwidth=2,
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
        widget.CurrentLayout(
            foreground=COLORS["fg"],
            background=COLORS["bg"],
            padding=2,
        ),
        widget.TextBox(
            text="|",
            foreground=COLORS["pink"],
            background=COLORS["bg"],
            padding=2,
        ),
        widget.WindowName(
            foreground=COLORS["fg"],
            background=COLORS["bg"],
            max_chars=20,
            width=150,
        ),
        widget.Spacer(),
        widget.CPUGraph(
            graph_color=COLORS["green"],
            background=COLORS["bg"],
            padding=3,
        ),
        widget.MemoryGraph(
            graph_color=COLORS["cyan"],
            background=COLORS["bg"],
            padding=3,
        ),
        widget.NetGraph(
            graph_color=COLORS["orange"],
            background=COLORS["bg"],
            padding=3,
        ),
        widget.ThermalSensor(
            foreground=COLORS["yellow"],
            background=COLORS["bg"],
            padding=3,
            threshold=80,
            fmt="🌡{}",
            show_short_text=False,
        ),
        widget.Battery(
            foreground=COLORS["green"],
            background=COLORS["bg"],
            padding=3,
            format="{char} {percent:2.0%}",
            low_foreground=COLORS["red"],
            charge_char="",
            discharge_char=" ",
            empty_char=" ",
            unknown_char="?",
            show_short_text=False,
        ),
        widget.Volume(
            foreground=COLORS["pink"],
            background=COLORS["bg"],
            padding=3,
            fmt="  {}",
        ),
        widget.Clock(
            format="%a %b %d  %H:%M",
            foreground=COLORS["purple"],
            background=COLORS["bg"],
            padding=3,
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
                background=COLORS["bg"],
                opacity=1,
                margin=[0, 0, 0, 0],
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

auto_fullscreen: bool = True
focus_on_window_activation: str = "smart"
reconfigure_screens: bool = True
auto_minimize: bool = True
wl_input_rules: str | None = None
wl_xcursor_theme: str | None = None
wl_xcursor_size: int = 24
