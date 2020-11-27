#! /usr/bin/env python

# -----------------------------------------------------------------------------
# includes
# -----------------------------------------------------------------------------

from dmenu_wrapper import run_dmenu

import os


# -----------------------------------------------------------------------------
# setup prompt and choices
# -----------------------------------------------------------------------------

prompt = "Take a break: "
choices = {
    "1. quite qtile": "qtile-cmd -o cmd -f shutdown",
    "2. sleep": "systemctl suspend; slock",
    "3. shutdown": "systemctl poweroff",
    "4. reboot": "systemctl reboot",
}


# -----------------------------------------------------------------------------
# action
# -----------------------------------------------------------------------------

if (run_dmenu(prompt, choices, os.path.basename(__file__))):
    run("qtile-cmd -o cmd -f restart", shell=True)


