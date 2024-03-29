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
    "1. sleep": "systemctl suspend",
    "2. shutdown": "systemctl poweroff",
    "3. reboot": "systemctl reboot",
}


# -----------------------------------------------------------------------------
# action
# -----------------------------------------------------------------------------

run_dmenu(prompt, choices, os.path.basename(__file__))


