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


def create_table_row(data: tuple, max_length: int = None, show_row_bottom_line: bool = True, header_row: bool = False):
    """create one row for the table."""
    COLUMNS = len(data)

    # now will find the word that have the max length of characters.
    # we will use the max length to center all the header titles strings.
    # and remember to add shifting/space value to get some space.
    SPACE_VALUE = 4

    row_separate_line = ("+" + "-"*max_length) * COLUMNS + "+\n"

    header_separate_line = ("=" + "="*max_length) * COLUMNS + "+\n"

    row_data = "|" + "|".join(str(title).center(max_length)
                              for title in data) + "|\n"

    if header_row:
        return header_separate_line + row_data + (header_separate_line * bool(show_row_bottom_line))

    return row_separate_line + row_data + (row_separate_line * bool(show_row_bottom_line))


def create_table(data: tuple, max_length: int = None):
    """create a cli table using ascii characters."""

    SPACE_VALUE = 4
    optimal_max_length = (find_max_length(data) + SPACE_VALUE)

    # guard conditions.
    if not max_length:
        # case is empty.
        max_length = optimal_max_length

    if max_length < optimal_max_length:
        max_length = optimal_max_length

    last_row = len(data) - 1

    for index, row in enumerate(data):
        print(create_table_row(row, max_length,
              show_row_bottom_line=(index == last_row), header_row=(index == 1)), end='')

    return None


def main():

    header_titles = "N", "Sample", 3, "HR", "FA", "EXP"
    header_titles1 = "1", "2", 4, "23", "222", "3213"
    header_titles2 = "2", "3", 5, "1", "113", "234"
    header_titles3 = "3", "4", 8, "43", "555", "66"

    t = (header_titles, header_titles1, header_titles2, header_titles3)

    create_table(t)


if __name__ == "__main__":
    main()
