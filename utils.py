"""
all the tools needed for the program to work.
"""


from os import name as OS_NAME
from os import system


def clear():
    """wipe the terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for all other system in the world.
        # system("your-command.")
        pass

    return None
