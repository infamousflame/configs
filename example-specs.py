# Device-specific configuration for qtile
# Copy this file to specs.py and customize for your system

# ============================================================================
# DISPLAY SETTINGS
# ============================================================================

# Wallpaper background image path (leave empty for solid color)
# Example: "/home/user/Pictures/wallpapers/mountain.png"
WALLPAPER = ""

# Fallback background color if no wallpaper is set (Qtile Hex format)
BACKGROUND_COLOR = "#1a1a2e"

# ============================================================================
# TERMINAL EMULATOR
# ============================================================================

# Your preferred terminal emulator
# Examples: "kitty", "alacritty", "st", "gnome-terminal", "konsole"
TERMINAL = "kitty"

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
# KEYBOARD SETTINGS
# ============================================================================

# Modifier key (mod4 = Super/Windows key, mod1 = Alt)
MOD = "mod4"

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

# ============================================================================
# BAR SETTINGS
# ============================================================================

# Bar height in pixels
BAR_HEIGHT = 24

# Bar background color (can be transparent with opacity)
BAR_BACKGROUND_COLOR = "#282a36"

# Bar position: "top" or "bottom"
BAR_POSITION = "top"

# ============================================================================
# APPLICATIONS (Optional)
# ============================================================================

# Browser launcher command
BROWSER = "firefox"

# File manager launcher command
FILE_MANAGER = "thunar"

# Application launcher (for dmenu-style launchers)
# Examples: "dmenu_run", "rofi -dmenu", "wofi --show drun"
LAUNCHER = "dmenu_run"

# Screenshot tool command
SCREENSHOT_CMD = "scrot"

# ============================================================================
# NOTIFICATION DAEMON
# ============================================================================

# Notification daemon to use
# Examples: "dunst", "mako", "none" (for no daemon)
NOTIFICATION_DAEMON = "dunst"
