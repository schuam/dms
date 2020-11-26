#! /usr/bin/env python

# -----------------------------------------------------------------------------
# includes
# -----------------------------------------------------------------------------

from dmenu_wrapper import run_dmenu
import os


# -----------------------------------------------------------------------------
# setup prompt and choices
# -----------------------------------------------------------------------------

prompt = "Say hello to: "
choices = {
    "1. Alice": "cd && echo 'Hello Alice!' > example.txt",
    "2. Bob": "cd && echo 'Hello Bob!' > example.txt",
}


# -----------------------------------------------------------------------------
# action
# -----------------------------------------------------------------------------

run_dmenu(prompt, choices, os.path.basename(__file__))

