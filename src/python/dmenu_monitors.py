#! /usr/bin/env python

# -----------------------------------------------------------------------------
# includes
# -----------------------------------------------------------------------------

from dmenu_wrapper import run_dmenu

from subprocess import run
import os


# -----------------------------------------------------------------------------
# constants
# -----------------------------------------------------------------------------

LAYOUT_SCRIPTS_DIR = "~/.local/share/screenlayouts"

LAYOUT_SCRIPT_PATHS = [
    os.path.join(LAYOUT_SCRIPTS_DIR, "laptop.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "laptop_plus_one_external.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "laptop_plus_two_external.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "laptop_plus_mirror.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "one_external.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "two_external.sh"),
]


# -----------------------------------------------------------------------------
# setup prompt and choices
# -----------------------------------------------------------------------------

prompt = "Change monitor settiong to: "
choices = {
    "1. laptop": LAYOUT_SCRIPT_PATHS[0],
    "2. laptop plus one external": LAYOUT_SCRIPT_PATHS[1],
    "3. laptop plus two external": LAYOUT_SCRIPT_PATHS[2],
    "4. laptop plus mirror": LAYOUT_SCRIPT_PATHS[3],
    "5. one external": LAYOUT_SCRIPT_PATHS[4],
    "6. two external": LAYOUT_SCRIPT_PATHS[5],
}


# -----------------------------------------------------------------------------
# action
# -----------------------------------------------------------------------------

if (run_dmenu(prompt, choices, os.path.basename(__file__))):
    run("qtile cmd-obj -o cmd -f restart", shell=True)
