# -----------------------------------------------------------------------------
# includes
# -----------------------------------------------------------------------------

from subprocess import run
import os


# -----------------------------------------------------------------------------
# constants
# -----------------------------------------------------------------------------

NOTIFICATION_TIME = 3000    # ms


# -----------------------------------------------------------------------------
# function definitions
# -----------------------------------------------------------------------------

def run_dmenu(prompt, choices, script_name=None):
    dmenu_choices = "\n".join(choices.keys())
    dmenu_cmd = 'echo -e "{}" | dmenu -i -l {:d} -p "{}"'.format(
            dmenu_choices, len(choices), prompt
    )

    success = False
    result = run(dmenu_cmd, shell=True, capture_output=True)
    if result.returncode == 0:
        chosen = result.stdout.decode("utf-8").rstrip()

        if chosen in choices.keys():
            success = True
            result = run(choices[chosen], shell=True)
        else:
            script = script_name
            if script == None:
                script = os.path.basename(__file__)

            notify_cmd = "notify-send -u low -t {:d} '{}' " \
                        "'You made an invalid choice!'".format(
                            NOTIFICATION_TIME, script
            )
            run(notify_cmd, shell=True)
    else:
        # The user quite dmenu by pressing <esc>, don't do anyhting, probably
        # no action is wanted. Especially don't send an annoying notification.
        pass

    return success

