"""

Docs;

"""
__version__ = 1.0

from tools import Tools


class Table:
    """
    draw Table on your terminal.

    draw_elements:str
        using this option you can change the draw elements that,
        is used to draw the table the default depend on your operating system:

          the default for window are:
            -> Horizontal-line: '-'
            -> Vertical-line: '|'
            -> Cross-point: '+'
            -> Special-Horizontal-Line for header: '='

          the default for *nix are:
            -

            for windows use "WIN" and for other machines,
            e.g. mac or linux use either "MAC" or "LINUX";

            by default the table will be drawn using the windows,
            elements;

        note: the Table will use only the four chars from any string.
            -> Horizontal-line: first-char of the string.
            -> Vertical-line: second-char of the string.
            -> Cross-point: third-char of the string.
            -> Special-Horizontal-Line for header: forth-char of the string.

        note: pass an string separated by space chars;

        if you pass string with less than four elements the Table will use the
        defaults for the remain ones for ex:
            passing "&X" => this will convert to "&X+="

        if you pass an empty string that will cause to use the,
        default draw_elements.

    special_header_line:bool
        using this option/flag you can draw the header line with,
        the Special-Horizontal-Line draw element that you pass, or
        using the default on the draw_element string.
        the default value of this flag is False.
        and it will draw the header line with the second draw-element
        like the rest of all horizontal lines.


    """

    # by the default we only ue those chars to build the table:
    #   ('+', '-', '|', '=')
    # and we can use some Special Uni-Code characters but this can make,
    # some bugs Especially for windows machines.
    __DEFAULT_DRAW_ELEMENTS = "- | + ="
    __LINUX_DRAW_ELEMENTS = "╭ ─ ┬ ╮ │ ┼ ┴ ╰ ╯ ┤ ├"
    __WINDOWS_DRAW_ELEMENTS = __DEFAULT_DRAW_ELEMENTS

    __DRAW_ELEMENTS_OPTIONS = ("WIN", "LINUX", "MAC")

    __DEFAULT_OS = "WIN" if Tools.MACHINE_OS_NAME == "windows" else "LINUX"

    def __init__(self, draw_element=__DEFAULT_OS, special_header_line=False):

        self.special_header_line = special_header_line

        self.draw_element = draw_element

        self.__table_header = []

        # guard conditions
        assert isinstance(
            self.draw_element, str), f"{self.draw_element} is {type(self.draw_element)} only {str} is allowed "

        assert self.draw_element in Table.__DRAW_ELEMENTS_OPTIONS, f"draw_element can only be one of {Table.__DRAW_ELEMENTS_OPTIONS}"

        if self.draw_element == "WIN":
            self.__horizontal_line, self.__vertical_line, self.__cross_point, self.__special_header_horizontal_line = Table.__DEFAULT_DRAW_ELEMENTS.split()
        else:
            # for mac and linux machines;
            self.__top_left_corner, self.__horizontal_line, self.__t_cross, self.__top_right_corner,\
                self.__vertical_line, self.__cross_point, self.__flipped_t_cross, self.__bottom_left_corner,\
                self.__bottom_right_corner, self.__right_side_cross, self.__left_side_cross = Table.__LINUX_DRAW_ELEMENTS.split()

    def __draw_header(self, max_string_len=20):
        """
        draw the table header on the terminal screen;
        """

        # first get the longest header string length;
        # so we can make sure that all our headers strings;
        # will fit good;
        longest_header_string_length = len(max(self.__table_header, key=len))

        headers_count = len(self.__table_header)

        # and make sure that our header strings don't go over the max_string_len
        if longest_header_string_length > max_string_len:
            longest_header_string_length = 20

        # to add space for the headers;
        SPACING = 4

        if self.draw_element == "WIN":
            # window machines;

            # first draw the upper line;
            upper_line = self.__cross_point + \
                f"{self.__cross_point}".join(
                    (self.__horizontal_line *
                     longest_header_string_length + self.__horizontal_line * SPACING)
                    for _ in range(headers_count)
                ) + self.__cross_point

            if self.special_header_line:
                # in case we want to use special char to draw the header line;
                self.__horizontal_line = self.__special_header_horizontal_line

            mid_line = self.__vertical_line + f"{self.__vertical_line}".join(
                header.center(longest_header_string_length+SPACING) for header in self.__table_header) + self.__vertical_line

            bottom_line = self.__cross_point + \
                f"{self.__cross_point}".join(
                    (self.__horizontal_line *
                     longest_header_string_length + self.__horizontal_line * SPACING)
                    for _ in range(headers_count)
                ) + self.__cross_point

            print(upper_line)
            print(mid_line)
            print(bottom_line)

        else:
            # linux machines;
            pass

        return None

    def show(self):
        """print the table on the terminal"""
        self.__draw_header()
        return None

    def show_table_header(self):
        """show the table header values"""

        return self.__table_header

    def __setitem__(self, key, value):
        """set self[key] to value"""

        if key == "header":
            self.__table_header.extend(value)

        return None


t = Table(draw_element="WIN", special_header_line=0)
t["header"] = ["count", "frequency", "item-name", "value", "price", "role"]
t.show()

# print(t.show_table_header())
