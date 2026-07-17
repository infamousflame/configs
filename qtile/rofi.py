from os import remove
from subprocess import Popen
from threading import Thread

from libqtile.lazy import lazy

from specs import COMMANDS

def cleanup():
    remove("/dev/shm/rofi.rasi")
    remove("/dev/shm/neon.rasi")

@lazy.function
def launcher(qtile):
    with open("/dev/shm/rofi.rasi", "w") as f:
        f.write(CONFIG)
    with open("/dev/shm/neon.rasi", "w") as f:
        f.write(THEME)

    def wait_and_cleanup():
        proc = Popen(COMMANDS.LAUNCHER)
        proc.wait()
        cleanup()

    Thread(target=wait_and_cleanup).start()


CONFIG = """configuration {
  modi: "drun,run,window";
  show-icons: true;
  icon-theme: "Papirus";
  font: "JetBrainsMono Nerd Font 12";
  terminal: "kitty";
}

@theme "neon"
"""

THEME = """* {
  bg: #0a0a12;
  bg-fill: rgba(10, 10, 18, 95%);
  fg: #ffffff;
  accent: #00f3ff;
  accent-alt: #ff00ff;
  border: #00f3ff;
  urgent: #ff2a2a;
}

window {
  width: 400px;
  background-color: @bg-fill;
  border: 2px solid;
  border-color: @border;
  border-radius: 12px;
  padding: 10px;
  shadow: true;
  shadow-color: @accent;
  shadow-offset: 0px 0px 15px;
}

mainbox {
  background-color: transparent;
  /* Removed 'prompt' from children to hide the 'drun' label entirely */
  children: [inputbar, message, listview];
  spacing: 10px;
}

inputbar {
  background-color: transparent; /* Fully transparent background */
  border-radius: 8px;
  padding: 8px;
  text-color: @fg; /* White text matches menu */
  children: [entry]; /* Drop the nested 'prompt' widget so "drun" text doesn't show */
}

/* Ensure the entry field (where you type) is transparent */
entry {
  background-color: transparent;
  text-color: @fg;
  cursor: text;
  placeholder: "Search apps...";
  placeholder-color: #6a6a8a;
}

/* Highlight text color when typing/focused */
entry selected {
  background-color: transparent;
  text-color: @accent;
}

message {
  background-color: transparent;
  text-color: @accent;
  margin: 5px 0;
}

listview {
  background-color: transparent;
  columns: 1;
  lines: 8;
  cycle: true;
  dynamic: true;
  scrollbar: false;
  layout: vertical;
  reverse: false;
  fixed-height: true;
  fixed-columns: true;
  spacing: 6px;
}

element {
  background-color: transparent;
  padding: 8px 10px;
  border-radius: 6px;
  text-color: @fg;
}

element-text {
  background-color: transparent;
  text-color: inherit;
}

element-icon {
  background-color: transparent;
  text-color: inherit;
}

element selected {
  background-color: transparent;
  border: 1px solid;
  text-color: @accent;
}

element-text selected {
  background-color: transparent;
  text-color: @accent;
}

element-icon selected {
  background-color: transparent;
  text-color: @accent;
}

element alternate {
  background-color: transparent;
}

element urgent {
  background-color: rgba(255, 42, 42, 0.2);
  text-color: #ffaaaa;
}
"""
