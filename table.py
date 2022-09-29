"""

Docs;

"""
__version__ = 1.0


class Table:
    """
    draw Table on your terminal.

    draw_element:str
        using this option you can change the draw elements that,
        is used to draw the table the default are:
            -> Horizontal-line: '-'
            -> Vertical-line: '|'
            -> Cross-point: '+'
            -> Special-Horizontal-Line for header: '='

        note: the Table will use only the four chars from any string.
            -> Horizontal-line: first-char of the string.
            -> Vertical-line: second-char of the string.
            -> Cross-point: third-char of the string.
            -> Special-Horizontal-Line for header: forth-char of the string.

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
    __DEFAULT_DRAW_ELEMENTS = "-|+="

    def __init__(self, draw_elements=__DEFAULT_DRAW_ELEMENTS, special_header_line=False):

        self.draw_elements = draw_elements
        self.special_header_line = special_header_line

        # guard conditions
        assert isinstance(
            draw_elements, str), f"{draw_elements} is {type(draw_elements)} only {str} is allowed "

        __draw_elements_len = len(draw_elements)
        if __draw_elements_len < 4:
            # even if the user pass an empty string this will use the default ones.
            self.draw_elements += Table.__DEFAULT_DRAW_ELEMENTS[__draw_elements_len:]

        self.horizontal_line, self.vertical_line, self.cross_point, self.special_header_horizontal_line = self.draw_elements


t = Table(draw_elements="ABT*")

print(t.horizontal_line)
print(t.vertical_line)
print(t.cross_point)
print(t.special_header_horizontal_line)
