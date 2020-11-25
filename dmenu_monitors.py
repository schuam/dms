#! /usr/bin/env python

from os.path import basename
import os
from dmenu_wrapper import run_dmenu
from subprocess import run


LAYOUT_SCRIPTS_DIR = "~/.dotfiles/.screenlayout"

layout_script_paths = [
    os.path.join(LAYOUT_SCRIPTS_DIR, "docked.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "mobile.sh"),
    os.path.join(LAYOUT_SCRIPTS_DIR, "one_external.sh"),
]

question = "Change monitor settiong to: "
choices = {
    "1. docked": layout_script_paths[0],
    "2. mobile": layout_script_paths[1],
    "3. one external": layout_script_paths[2],
}

if (run_dmenu(question, choices, basename(__file__))):
    run("qtile-cmd -o cmd -f restart", shell=True)

