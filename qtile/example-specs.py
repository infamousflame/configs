# Device-specific configuration for qtile
# Copy this file to specs.py and customize for your system


# ============================================================================
# KEYBOARD SETTINGS
# ============================================================================

# Modifier key (mod4 = Super/Windows key, mod1 = Alt)
MOD = "mod4"

class KEYS:
    LEFT, DOWN, UP, RIGHT = "hjkl"
    TERMINAL = "Return"
    LAUNCHER = "x"
    BROWSER = "b"
    FILE_MANAGER = "f"
    SYSTEM_MONITOR = "s"
    KILL = "w"
    NORMALIZE = "n"
    FLOAT = "f"
    RESTART = "r"
    LOGOUT = "q"
    COPY = "c"
    PASTE = "v"



# ============================================================================
# DISPLAY SETTINGS
# ============================================================================

# Maximum number of monitors you need
SCREENS: int = 2

# Wallpaper background image path(s) (leave empty for solid color)
# Examples: "/home/user/Pictures/wallpapers/mountain.png"
#           ["/path/to/wp1.png", "/path/to/wp2.jpg"]  # Multiple wallpapers rotate
WALLPAPER: list[str] = []

# Wallpaper switch period in seconds (0 to disable rotation)
WALLPAPER_SWITCH_PERIOD: int = 0

# Fallback background color if no wallpaper is set (Qtile Hex format)
BACKGROUND_COLOR = "#1a1a2e"


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

# Border color for focused window
FOCUSED_BORDER_COLOR = "#bd93f9"  # Dracula purple

# Border color for unfocused windows
UNFOCUSED_BORDER_COLOR = "#44475a"  # Dracula gray

# ============================================================================
# COLORSCHEME (Dracula-inspired)
# ============================================================================

# These colors are used throughout the config for consistent theming
COLORS = {
    "bg": "#282a36",           # Background (dark)
    "fg": "#f8f8f2",           # Foreground (light text)
    "selected_bg": "#44475a",  # Selection/hover background
    "selected_fg": "#f8f8f2",  # Selection/hover foreground
    "cyan": "#8be9fd",         # Cyan accent
    "green": "#50fa7b",        # Green accent
    "orange": "#ffb86c",       # Orange accent
    "pink": "#ff79c6",         # Pink accent
    "purple": "#bd93f9",       # Purple accent
    "red": "#ff5555",          # Red accent
    "yellow": "#f1fa8c",       # Yellow accent
}

# ============================================================================
# WORKSPACE/GROUP SETTINGS
# ============================================================================

# Names for your workspace groups
# Common setup: 3 groups for work, coding, and misc
GROUPS = ["1: term", "2: web", "3: code", "4: misc"]

# ============================================================================
# WIDGET SETTINGS
# ============================================================================

# Widget padding (space between elements)
WIDGET_PADDING = 10

# Widget corner radius (for rounded appearance)
WIDGET_ROUNDED = 5

# System tray icon size
TRAY_ICON_SIZE = 16

# Network interface (leave empty for auto-detect)
# Run `ip link` or `ip addr` to find your interface
# Examples: "wlp2s0", "eth0", "enp0s3"
NET_INTERFACE: str = ""

# ============================================================================
# BAR SETTINGS
# ============================================================================

# Bar height in pixels
BAR_HEIGHT = 40

# Bar background color (can be transparent with opacity)
BAR_BACKGROUND_COLOR = "#282a36"

# Bar position: "top" or "bottom"
BAR_POSITION = "top"

# ============================================================================
# COMMANDS
# ============================================================================

class COMMANDS:
    # Terminal emulator
    TERMINAL = "kitty"
    # System monitor
    SYSTEM_MONITOR = "btop"
    # Browser
    BROWSER = "firefox"
    # File manager
    FILE_MANAGER = "thunar"
    # Application launcher
    LAUNCHER = "dmenu_run"
    # Screenshot tool
    SCREENSHOT = "slurp | grim -g - - | wl-copy --type image/png"
    SCREENSHOT_ANNOTATE = "slurp | grim -g - - | swappy -f - -o -"
    # Lock screen
    LOCK = "xscreensaver-command -lock"
    # Notification daemon
    NOTIFICATION_DAEMON = "dunst"

    # Startup autostart commands
    STARTUP_KEYRING = ["/usr/bin/gnome-keyring-daemon", "--start", "--components=secrets"]
    STARTUP_CLIPBOARD_TEXT = ["wl-paste", "--type", "text", "--watch", "cliphist", "store"]
    STARTUP_CLIPBOARD_IMAGE = ["wl-paste", "--type", "image", "--watch", "cliphist", "store"]
