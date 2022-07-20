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


# clear()

# we only use those chars to build the table.
# '+', '-', '|', '=', and we can use Special,
# Uni-code characters but this can make some bugs,
# Especially for windows machines.


def find_max_length(data: tuple):
    """find the max string length in given data,
    and return the max length as int.
    in wrong cases return '-1' as int."""

    # Guard conditions.
    if not data:
        # empty case.
        return -1

    max_string = max(data, key=lambda a: len(str(a)))

    return len(max_string)


def create_table_row(data: tuple, max_length: int = None, show_row_bottom_line: bool = True):
    """create a cli table using ascii characters."""

    COLUMNS = len(data)

    # now will find the word that have the max length of characters.
    # we will use the max length to center all the header titles strings.
    # and remember to add shifting/space value to get some space.
    SPACE_VALUE = 4

    max_length = (find_max_length(data) +
                  SPACE_VALUE) if not max_length else max_length

    header_separate_line = ("+" + "-"*max_length) * COLUMNS + "+\n"

    header_data = "|" + "|".join(str(title).center(max_length)
                                 for title in data) + "|\n"

    return header_separate_line + header_data + (header_separate_line * bool(bottom_row_line))


def main():

    header_titles = "N", "Sample", 3, "HR", "FA", "EXP"
    print(create_table_cells(header_titles, bottom_row_line=0), end="")
    print(create_table_cells(header_titles), end="")


if __name__ == "__main__":
    main()
