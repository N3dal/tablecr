"""
all the tools needed for the program to work.
"""


from os import name as OS_NAME
from os import system


class Tools:
    """"""
    @staticmethod
    def clear():
        """wipe the terminal screen."""

        if os_name == "posix":
            # for *nix machines.
            system("clear")

        elif os_name == "windows":
            system("cls")

        else:
            # for all other system in the world.
            # system("your-command.")
            pass

        return None
