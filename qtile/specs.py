# Device-specific configuration for qtile
# Copy this file to specs.py and customize for your system


# ============================================================================
# KEYBOARD SETTINGS
# ============================================================================

# Modifier key (mod4 = Super/Windows key, mod1 = Alt)
MOD = "mod4"

class KEYS:
    LEFT, DOWN, UP, RIGHT = "uiop"
    TERMINAL = "Return"
    LAUNCHER = "x"
    BROWSER = "b"
    FILE_MANAGER = "f"
    SYSTEM_MONITOR = "s"
    KILL = "w"
    NORMALIZE = "n"
    FLOAT = "f"
    RESTART = "r"
    LOGOUT = "l"
    CAPTURE = "c"



# ============================================================================
# DISPLAY SETTINGS
# ============================================================================

# Maximum number of monitors you need
SCREENS: int = 2

# Wallpaper background image path(s) (leave empty for solid color)
# Examples: "/home/user/Pictures/wallpapers/mountain.png"
#           ["/path/to/wp1.png", "/path/to/wp2.jpg"]  # Multiple wallpapers rotate
WALLPAPER: list[str] = ["/usr/share/backgrounds/f44/default/f44-01-night.jxl", "/usr/share/backgrounds/f44/default/f44-01-day.jxl"]

# Wallpaper switch period in seconds (0 to disable rotation)
WALLPAPER_SWITCH_PERIOD: int = 3600

# ============================================================================
# FONTS
# ============================================================================

# Main font for bars and widgets
# Format: "Font Name [size]"
FONT_NAME = "JetBrains Mono"
FONT_SIZE = 12

# Icon font size (usually smaller)
ICON_SIZE = 14

# ============================================================================
# LAYOUT THEMING
# ============================================================================

# Border width for focused windows (pixels)
BORDER_WIDTH = 2

# ============================================================================
# COLORSCHEME (Dracula-inspired)
# ============================================================================

# These colors are used throughout the config for consistent theming
COLORS = {
    "bg": "#282a36",                # Background (dark)
    "fg": "#f8f8f2",                # Foreground (light text)
    "selected_bg": "#44475a",       # Selection/hover background
    "selected_fg": "#f8f8f2",       # Selection/hover foreground
    "cyan": "#8be9fd",              # Cyan accent
    "green": "#50fa7b",             # Green accent
    "orange": "#ffb86c",            # Orange accent
    "pink": "#ff79c6",              # Pink accent
    "purple": "#bd93f9",            # Purple accent
    "red": "#ff5555",               # Red accent
    "yellow": "#f1fa8c",            # Yellow accent
    "focused_border": "#bd93f9",    # Dracula purple
    "unfocused_border": "#44475a",  # Dracula gray
}

# ============================================================================
# WORKSPACE/GROUP SETTINGS
# ============================================================================

# Names for your workspace groups
# Common setup: 3 groups for work, coding, and misc
GROUPS = [str(x) for x in range(1, 10)]

# ============================================================================
# WIDGET SETTINGS
# ============================================================================

# Widget padding (space between elements)
WIDGET_PADDING = 10

# Widget corner radius (for rounded appearance)
WIDGET_ROUNDED = 5

# ============================================================================
# BAR SETTINGS
# ============================================================================

# Bar height in pixels
BAR_HEIGHT = 40

# ============================================================================
# COMMANDS
# ============================================================================

class COMMANDS:
    # Terminal emulator
    TERMINAL = "kitty"
    # System monitor
    SYSTEM_MONITOR = "btop"
    # Browser
    BROWSER = "brave-origin"
    # File manager
    FILE_MANAGER = "pcmanfm"
    # Application launcher
    LAUNCHER = "rofi -show drun"
    # Screenshot tool
    SCREENSHOT = "slurp | grim -g - - | wl-copy --type image/png"
    SCREENSHOT_ANNOTATE = "slurp | grim -g - - | swappy -f - -o -"
    # Lock screen
    LOCK = "hyprlock --config /dev/shm/hyprlock.conf"

    # Startup autostart commands
    STARTUP = [
        ["/usr/bin/gnome-keyring-daemon", "--start", "--components=secrets"],
        ["wl-paste", "--type", "text", "--watch", "cliphist", "store"],
        ["wl-paste", "--type", "image", "--watch", "cliphist", "store"],
    ]
