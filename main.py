#!/usr/bin/python3
# -----------------------------------------------------------------
# simple script to create tables in cli using ascii characters.
#
#
#
# Author:N84.
#
# Create Date:Wed Nov 24 21:25:20 2021.
# ///
# ///
# ///
# -----------------------------------------------------------------

# todo:
# update this piece of shit.


from os import system
from os import name as os_name


def clear():
    """wipe the terminal."""

    if os_name == "posix":
        # for *nix machines.
        system("clear")

    elif os_name == "windows":
        system("cls")

    else:
        # for all other system in the world.
        # system("your-command.")
        pass


clear()

# we only use those chars to build the table.
# '+', '-', '|', '=', and we can use nice,
# unicode chars like that i use in xo game.


def create_table_header(header_titles: tuple, max_length: int = None):
    """create a cli table using ascii characters."""

    COLUMNS = len(header_titles)

    # now will find the word that have the max length of characters.
    # we will use the max length to center all the header titles strings.
    # and remember to add shifthing/space value to get some space.
    SPACE_VALUE = 4
    MAX_LENGTH = (len(max(header_titles, key=lambda a: len(str(a)))) +
                  SPACE_VALUE) if not max_length else max_length

    header_separate_line = ("+" + "-"*MAX_LENGTH) * COLUMNS + "+\n"
    header_data = "|" + "|".join(str(title).center(MAX_LENGTH)
                                 for title in header_titles) + "|\n"

    return header_separate_line + header_data + header_separate_line


def create_table_data_cells(data: tuple, header_titles: tuple):
    """"""

    # we will use header_titles to calc the columns count,
    COLUMNS = len(header_titles)

    data_separate_line = ("+" + "-"*MAX_LENGTH) * COLUMNS + "+\n"


def main():

    header_titles = "N", "Sample", 3, "HR", "FA", "EXP"
    print(create_table_header(header_titles), end="")


if __name__ == "__main__":
    main()
