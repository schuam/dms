#! /usr/bin/env python

# -----------------------------------------------------------------------------
# includes
# -----------------------------------------------------------------------------

from os.path import basename
import os
from dmenu_wrapper import run_dmenu
from subprocess import run


# -----------------------------------------------------------------------------
# constants
# -----------------------------------------------------------------------------

LAYOUT_SCRIPTS_DIR = "~/workspaces/screenlayouts"

LAYOUT_SCRIPT_PATHS = [
    os.path.join(LAYOUT_SCRIPTS_DIR, "docked.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "mobile.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "one_external.sh"),
]


# -----------------------------------------------------------------------------
# setup prompt and choices
# -----------------------------------------------------------------------------

prompt = "Change monitor settiong to: "
choices = {
    "1. docked": LAYOUT_SCRIPT_PATHS[0],
    "2. mobile": LAYOUT_SCRIPT_PATHS[1],
    "3. one external": LAYOUT_SCRIPT_PATHS[2],
}


# -----------------------------------------------------------------------------
# action
# -----------------------------------------------------------------------------

if (run_dmenu(prompt, choices, basename(__file__))):
    run("qtile-cmd -o cmd -f restart", shell=True)

