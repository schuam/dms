#! /usr/bin/env python

from subprocess import check_output
from subprocess import call

question = "What's up dude? "
choices = {
    "test a": "mkdir a; mkdir z",
    "test b": "mkdir b; mkdir y",
}

d_choises = "\n".join(choices.keys())
d_cmd = 'echo -e "{}" | dmenu -i -l {:d} -p "{}"'.format(
        d_choises, len(choices), question
)

chosen = check_output(d_cmd, shell=True).decode("utf-8").rstrip()
call(choices[chosen], shell=True)

