#! /usr/bin/env python

from subprocess import run
from os.path import basename
import os


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

question = "Screenshot will be saved in {}: ".format(IMG_DIR)
choices = {
    "1. quick fullscreen": \
            COMMAND_TEMPLATE.format("-d 1", FULLSCREEN_NOTIFICATION),
    "2. delayed fullscreen": \
            COMMAND_TEMPLATE.format("-d 4", FULLSCREEN_NOTIFICATION),
    "3. selection": \
            COMMAND_TEMPLATE.format("-s ", SECTION_NOTIFICATION),
}

d_choises = "\n".join(choices.keys())
d_cmd = 'echo -e "{}" | dmenu -i -l {:d} -p "{}"'.format(
        d_choises, len(choices), question
)

result = run(d_cmd, shell=True, capture_output=True)
if result.returncode == 0:
    chosen = result.stdout.decode("utf-8").rstrip()

    if chosen in choices.keys():
        result = run(choices[chosen], shell=True)
    else:
        notify_cmd = "notify-send -u low -t {:d} '{}' " \
                     "'You made an invalid choice!'".format(
                     NOTIFICATION_TIME, basename(__file__))
        run(notify_cmd, shell=True)
else:
    # The user quite dmenu by pressing <esc>, don't do anyhting, probably no
    # action is wanted. Especially don't send an annoying notification.
    pass

