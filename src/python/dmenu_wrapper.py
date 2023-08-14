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
# helper function definitions
# -----------------------------------------------------------------------------

def _promt_user(prompt, choices):
    dmenu_choices = "\n".join(choices.keys())
    dmenu_cmd = 'echo -e "{}" | dmenu -i -l {:d} -p "{}"'.format(
            dmenu_choices, len(choices), prompt
    )

    return run(dmenu_cmd, shell=True, capture_output=True)


def _act_on_users_decision(choices, decision, script_name=None):
    success = False
    if decision.returncode == 0:
        chosen = decision.stdout.decode("utf-8").rstrip()

        if chosen in choices.keys():
            success = True
            run(choices[chosen], shell=True)
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


# -----------------------------------------------------------------------------
# api function definitions
# -----------------------------------------------------------------------------

def run_dmenu(prompt, choices, script_name=None):
    """
    Ask user what to do and do it.

    This is a wrapper around dmenu. It runs dmenu with the passed in prompt and
    choices (menu entries) and afterwards executes what the user wants.

    Keyword arguments:
    prompt :      String that will be used in dmenu as the user prompt
    choices :     A python dictonary that has the possible choices. The keys
                  must be strings. These strings will be presented to the user
                  as choices to chose from. The values of the dictonary must
                  also be strings. These scrings must either be a command (or a
                  series of commands, that can be run in a shell, or a script
                  that can be run in a shell and is callable (either the
                  absolut path to the script or the name of a script, that is
                  located in the users PATH.
    script_name : The name of the calling script. This is used in case the user
                  puts in something into dmenu that is not a valid choice. In
                  this case a notification is issued that has shows the
                  **script_name**. If no script_name is passed, the name of
                  this very file is used instead.
    """
    decision = _promt_user(prompt, choices)
    return _act_on_users_decision(choices, decision, script_name)

