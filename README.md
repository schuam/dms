# dms (dmenu scripts)

This repo contains a wrapper around [dmenu](https://tools.suckless.org/dmenu/)
and my collection of dmenu scripts. Everything written in python.


## Background

A little while ago I came across dmenu and started using it as my default
application launcher. But actually you can do more with it, than just
launching programs. It's actually a 'dynamic menu', which allows you to present
a prompt to the user and let them select an one option from a list of choices.
Once the user has made a decision, some action depending on the users decision
can be triggered. In order to realize such a menu, you have to write a dmenu
script.

While I liked the idea and what you could do with dmenu, I didn't like to write
my dmenu scripts in bash, which seems to be what most people do. Of course bash
is a good solution to do that, it's just that my bash skills are very limited
and I just hate the syntax of bash. I wanted a way to be able to easily define
a prompt, the available options to chose from, and the different actions that
should be taken.


## Solution

I wrote a simple wrapper around dmenu in python. You can check it out
[here](./src/dmenu_wrapper.py). It contains a function with three arguments:

```python
run_dmenu(prompt, choises, script_name=None)
```

Now I can write very simple python dmenu scripts. All I have to do is define
the prompt (as a string):

```python
prompt = "Say hello to: "
```

and the choices the user may chose from (as a dictionary):

```python
choices = {
    "1. Alice": "cd && echo 'Hello Alice!' > example.txt",
    "2. Bob": "cd && echo 'Hello Bob!' > example.txt",
}
```

The only step left is call the wrapper function:

```python
run_dmenu(prompt, choices, "example")
```

Check out the whole example [here](./src/dmenu_example.py).


## Requirements

I run all of this on a Linux (Arch Linux) machine. I guess this should also
work on other operation system, but I haven't tested it.

But you definitely need:

- **dmenu**: Well, this should be obvious :-)
- **python**: Version 3.5 or higher. The wrapper uses the function
              subprocess.run, which was added in python 3.5.

I put my dmenu scripts in a directory that is part of my PATH and setup
keyboard short cuts to trigger them. But I guess there are other ways to do it.
Important is, that the wrapper script is in the same directory as the other
scripts.

