#! /usr/bin/env python

# -----------------------------------------------------------------------------
# includes
# -----------------------------------------------------------------------------

from os.path import basename
import os
from dmenu_wrapper import run_dmenu


# -----------------------------------------------------------------------------
# constants
# -----------------------------------------------------------------------------

NOTIFICATION_TIME = 3000    # ms
IMG_DIR = "$XDG_PICTURES_DIR/screenshots"
IMG_NAME = "scrot_%Y-%m-%d_%H-%M-%S.png"
IMG_PATH = os.path.join(IMG_DIR, IMG_NAME)
FULLSCREEN_NOTIFICATION = "Fullscreen taken and saved"
SECTION_NOTIFICATION = "Scetion screenshot taken and saved"
COMMAND_TEMPLATE = "scrot -z {} {} && " \
                   "notify-send -u low -t {} 'Scrot' '{}'".format(
                        "{}", IMG_PATH, NOTIFICATION_TIME, "{}"
)


# -----------------------------------------------------------------------------
# setup prompt and choices
# -----------------------------------------------------------------------------

prompt = "Screenshot will be saved in {}: ".format(IMG_DIR)
choices = {
    "1. quick fullscreen": \
            COMMAND_TEMPLATE.format("-d 1", FULLSCREEN_NOTIFICATION),
    "2. delayed fullscreen": \
            COMMAND_TEMPLATE.format("-d 4", FULLSCREEN_NOTIFICATION),
    "3. selection": \
            COMMAND_TEMPLATE.format("-s ", SECTION_NOTIFICATION),
}


# -----------------------------------------------------------------------------
# action
# -----------------------------------------------------------------------------

run_dmenu(prompt, choices, basename(__file__))

