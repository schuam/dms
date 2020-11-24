#! /usr/bin/env python

from subprocess import run
from os.path import basename


NOTIFICATION_TIME = 3000    # ms

question = "What's up dude? "
choices = {
    "test a": "mkdir a; mkdir z",
    "test b": "mkdir b; mkdir y",
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

