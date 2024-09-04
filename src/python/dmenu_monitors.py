#! /usr/bin/env python

# -----------------------------------------------------------------------------
# includes
# -----------------------------------------------------------------------------

from dmenu_wrapper import run_dmenu

from socket import gethostname
import os


# -----------------------------------------------------------------------------
# constants
# -----------------------------------------------------------------------------

HOSTNAME = gethostname()
LAYOUT_SCRIPTS_DIR = "~/.local/share/screenlayouts"

LAYOUT_SCRIPT_PATHS = [
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-1_external-0.sh".format(HOSTNAME)),
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-1_external-1.sh".format(HOSTNAME)),
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-1_external-2.sh".format(HOSTNAME)),
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-1_external-3.sh".format(HOSTNAME)),
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-1_mobile-1.sh".format(HOSTNAME)),
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-1_external-1_mirror.sh".format(HOSTNAME)),
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-0_external-1.sh".format(HOSTNAME)),
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-0_external-2.sh".format(HOSTNAME)),
    os.path.join(LAYOUT_SCRIPTS_DIR, "{}_internal-0_external-3.sh".format(HOSTNAME)),
]


# -----------------------------------------------------------------------------
# setup prompt and choices
# -----------------------------------------------------------------------------

prompt = "Change monitor settiong to: "
choices = {
    "1. laptop": LAYOUT_SCRIPT_PATHS[0],
    "2. laptop plus one external": LAYOUT_SCRIPT_PATHS[1],
    "3. laptop plus two external": LAYOUT_SCRIPT_PATHS[2],
    "4. laptop plus three external": LAYOUT_SCRIPT_PATHS[3],
    "5. laptop plus one mobile": LAYOUT_SCRIPT_PATHS[4],
    "6. laptop plus mirror": LAYOUT_SCRIPT_PATHS[5],
    "7. one external": LAYOUT_SCRIPT_PATHS[6],
    "8. two external": LAYOUT_SCRIPT_PATHS[7],
    "9. three external": LAYOUT_SCRIPT_PATHS[8],
}


# -----------------------------------------------------------------------------
# action
# -----------------------------------------------------------------------------

if (run_dmenu(prompt, choices, os.path.basename(__file__))):
    if os.system("ps -e | grep xmonad") == 0:
        os.system("xmonad --restart")
    else:
        os.system("qtile cmd-obj -o cmd -f restart")
