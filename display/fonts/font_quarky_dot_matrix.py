# This font designed by Michael Chan using inspiration from:
# * DotMatrix (https://www.urbanfonts.com/fonts/DotMatrix.font) for lowercase
# * Quarky (https://cooltext.com/Fonts-Dot-Matrix) for uppercase
# * Atari Small (https://hea-www.harvard.edu/~fine/Tech/atari-small.bdf) other.
# Designed with http://dotmatrixtool.com/# : 4x8px, column major, little endian.

from font import Font

class FontQuarkyDotMatrix(Font):

    def __init__(self):
        Font.__init__(self)

    def getWidth(self):
        return 4

    def getHeight(self):
        return 8

    def getPixel(self, x, y):
        return (font_bitmap[self.mChar][x] & (1 << (y)))


font_bitmap = {
" " : [
    #    32 ' ' |01234567|
    0x00, #    0|        |
    0x00, #    1|        |
    0x00, #    2|        |
    0x00, #    3|        |
],
"!" : [
    #    33 '!' |01234567|
    0x00, #    0|        |
    0x5E, #    1| # #### |
    0x00, #    2|        |
    0x00, #    3|        |
],
"\"" : [
    #    34 '"' |01234567|
    0x06, #    0|     ## |
    0x00, #    1|        |
    0x06, #    2|     ## |
    0x00, #    3|        |
],
"#" : [
    #    35 '#' |01234567|
    0x7E, #    0| ###### |
    0x24, #    1|  #  #  |
    0x7E, #    2| ###### |
    0x00, #    3|        |
],
"$" : [
    #    36 '$' |01234567|
    0x24, #    0|  #  #  |
    0xCB, #    1|##  # ##|
    0x34, #    2|  ## #  |
    0x00, #    3|        |
],
"%" : [
    #    37 '%' |01234567|
    0x62, #    0| ##   # |
    0x18, #    1|   ##   |
    0x46, #    2| #   ## |
    0x00, #    3|        |
],
"&" : [
    #    38 '&' |01234567|
    0x3A, #    0|  ### # |
    0x65, #    1| ##  # #|
    0x5A, #    2| # ## # |
    0x00, #    3|        |
],
"'" : [
    #    39 ''' |01234567|
    0x00, #    0|        |
    0x06, #    1|     ## |
    0x00, #    2|        |
    0x00, #    3|        |
],
"(" : [
    #    40 '(' |01234567|
    0x00, #    0|        |
    0x3C, #    1|  ####  |
    0x42, #    2| #    # |
    0x00, #    3|        |
],
")" : [
    #    41 ')' |01234567|
    0x42, #    0| #    # |
    0x3C, #    1|  ####  |
    0x00, #    2|        |
    0x00, #    3|        |
],
"*" : [
    #    42 '*' |01234567|
    0x2A, #    0|  # # # |
    0x1C, #    1|   ###  |
    0x2A, #    2|  # # # |
    0x00, #    3|        |
],
"+" : [
    #    43 '+' |01234567|
    0x08, #    0|    #   |
    0x3E, #    1|  ##### |
    0x08, #    2|    #   |
    0x00, #    3|        |
],
"," : [
    #    44 ',' |01234567|
    0x80, #    0|#       |
    0x60, #    1| ##     |
    0x00, #    2|        |
    0x00, #    3|        |
],
"-" : [
    #    45 '-' |01234567|
    0x08, #    0|    #   |
    0x08, #    1|    #   |
    0x08, #    2|    #   |
    0x00, #    3|        |
],
"." : [
    #    46 '.' |01234567|
    0x00, #    0|        |
    0x60, #    1| ##     |
    0x00, #    2|        |
    0x00, #    3|        |
],
"/" : [
    #    47 '/' |01234567|
    0x60, #    0| ##     |
    0x18, #    1|   ##   |
    0x06, #    2|     ## |
    0x00, #    3|        |
],
"0" : [
    #    48 '0'
    0x3e, 0x41, 0x41, 0x3e
],
"1" : [
    #    49 '1'
    0x00, 0x42, 0x7f, 0x40
],
"2" : [
    #    50 '2'
    0x72, 0x51, 0x49, 0x46
],
"3" : [
    #    51 '3'
    0x22, 0x49, 0x49, 0x36
],
"4" : [
    #    52 '4'
    0x07, 0x08, 0x08, 0x7f
],
"5" : [
    #    53 '5'
    0x27, 0x45, 0x45, 0x39
],
"6" : [
    #    54 '6'
    0x3e, 0x49, 0x49, 0x30
],
"7" : [
    #    55 '7'
    0x01, 0x71, 0x0d, 0x03
],
"8" : [
    #    56 '8'
    0x36, 0x49, 0x49, 0x36
],
"9" : [
    #    57 '9'
    0x06, 0x49, 0x49, 0x3e
],
":" : [
    #    58 ':' |01234567|
    0x00, #    0|        |
    0x24, #    1|  #  #  |
    0x00, #    2|        |
    0x00, #    3|        |
],
";" : [
    #    59 ';' |01234567|
    0x40, #    0| #      |
    0x24, #    1|  #  #  |
    0x00, #    2|        |
    0x00, #    3|        |
],
"<" : [
    #    60 '<' |01234567|
    0x10, #    0|   #    |
    0x28, #    1|  # #   |
    0x44, #    2| #   #  |
    0x00, #    3|        |
],
"=" : [
    #    61 '=' |01234567|
    0x14, #    0|   # #  |
    0x14, #    1|   # #  |
    0x14, #    2|   # #  |
    0x00, #    3|        |
],
">" : [
    #    62 '>' |01234567|
    0x44, #    0| #   #  |
    0x28, #    1|  # #   |
    0x10, #    2|   #    |
    0x00, #    3|        |
],
"?" : [
    #    63 '?' |01234567|
    0x04, #    0|     #  |
    0x52, #    1| # #  # |
    0x0C, #    2|    ##  |
    0x00, #    3|        |
],
"@" : [
    #    64 '@' |01234567|
    0x3C, #    0|  ####  |
    0x42, #    1| #    # |
    0x4C, #    2| #  ##  |
    0x00, #    3|        |
],
"A" : [
    #    65 'A'
    0x7e, 0x09, 0x09, 0x7e
],
"B" : [
    #    66 'B'
    0x7f, 0x49, 0x49, 0x36
],
"C" : [
    #    67 'C'
    0x3e, 0x41, 0x41, 0x22
],
"D" : [
    #    68 'D'
    0x7f, 0x41, 0x41, 0x3e
],
"E" : [
    #    69 'E'
    0x7f, 0x49, 0x49, 0x41
],
"F" : [
    #    70 'F'
    0x7f, 0x09, 0x09, 0x01
],
"G" : [
    #    71 'G'
    0x3e, 0x41, 0x49, 0x39
],
"H" : [
    #    72 'H'
    0x7f, 0x08, 0x08, 0x7f
],
"I" : [
    #    73 'I'
    0x00, 0x41, 0x7f, 0x41
],
"J" : [
    #    74 'J'
    0x20, 0x40, 0x41, 0x3f
],
"K" : [
    #    75 'K'
    0x7f, 0x08, 0x14, 0x63
],
"L" : [
    #    76 'L'
    0x7f, 0x40, 0x40, 0x40
],
"M" : [
    #    77 'M'
    0x7f, 0x02, 0x02, 0x7f
],
"N" : [
    #    78 'N'
    0x7f, 0x06, 0x18, 0x7f
],
"O" : [
    #    79 'O'
    0x3e, 0x41, 0x41, 0x3e
],
"P" : [
    #    80 'P'
    0x7f, 0x09, 0x09, 0x06
],
"Q" : [
    #    81 'Q'
    0x3e, 0x41, 0x41, 0xbe
],
"R" : [
    #    82 'R'
    0x7f, 0x09, 0x09, 0x76
],
"S" : [
    #    83 'S'
    0x46, 0x49, 0x49, 0x31
],
"T" : [
    #    84 'T'
    0x00, 0x01, 0x7f, 0x01
],
"U" : [
    #    85 'U'
    0x3f, 0x40, 0x40, 0x3f
],
"V" : [
    #    86 'V'
    0x1f, 0x60, 0x60, 0x1f
],
"W" : [
    #    87 'W'
    0x7f, 0x20, 0x20, 0x7f
],
"X" : [
    #    88 'X'
    0x77, 0x08, 0x08, 0x77
],
"Y" : [
    #    89 'Y'
    0x47, 0x48, 0x48, 0x3f
],
"Z" : [
    #    90 'Z'
    0x62, 0x52, 0x4a, 0x46
],
"[" : [
    #    91 '[' |01234567|
    0x00, #    0|        |
    0x7E, #    1| ###### |
    0x42, #    2| #    # |
    0x00, #    3|        |
],
"\\" : [
    #    92 '\' |01234567|
    0x06, #    0|     ## |
    0x18, #    1|   ##   |
    0x60, #    2| ##     |
    0x00, #    3|        |
],
"]" : [
    #    93 ']' |01234567|
    0x42, #    0| #    # |
    0x7E, #    1| ###### |
    0x00, #    2|        |
    0x00, #    3|        |
],
"^" : [
    #    94 '^' |01234567|
    0x04, #    0|     #  |
    0x02, #    1|      # |
    0x04, #    2|     #  |
    0x00, #    3|        |
],
"_" : [
    #    95 '_' |01234567|
    0x80, #    0|#       |
    0x80, #    1|#       |
    0x80, #    2|#       |
    0x80, #    3|#       |
],
"`" : [
    #    96 '`' |01234567|
    0x02, #    0|      # |
    0x04, #    1|     #  |
    0x00, #    2|        |
    0x00, #    3|        |
],
"a" : [
    #    97 'a'
    0x30, 0x4a, 0x4a, 0x7c
],
"b" : [
    #    98 'b'
    0x7e, 0x48, 0x48, 0x30
],
"c" : [
    #    99 'c'
    0x38, 0x44, 0x44, 0x44
],
"d" : [
    #   100 'd'
    0x30, 0x48, 0x48, 0x7e
],
"e" : [
    #   101 'e'
    0x38, 0x54, 0x54, 0x58
],
"f" : [
    #   102 'f'
    0x44, 0x7e, 0x45, 0x01
],
"g" : [
    #   103 'g'
    0x0c, 0x52, 0x52, 0x3e
],
"h" : [
    #   104 'h'
    0x7e, 0x08, 0x08, 0x70
],
"i" : [
    #   105 'i'
    0x00, 0x44, 0x7d, 0x40
],
"j" : [
    #   106 'j'
    0x80, 0x84, 0x7d, 0x00
],
"k" : [
    #   107 'k'
    0x7e, 0x10, 0x28, 0x44
],
"l" : [
    #   108 'l'
    0x00, 0x42, 0x7e, 0x40
],
"m" : [
    #   109 'm'
    0x7c, 0x08, 0x08, 0x7c
],
"n" : [
    #   110 'n'
    0x7c, 0x08, 0x04, 0x78
],
"o" : [
    #   111 'o'
    0x38, 0x44, 0x44, 0x38
],
"p" : [
    #   112 'p'
    0xfc, 0x24, 0x24, 0x18
],
"q" : [
    #   113 'q'
    0x18, 0x24, 0x24, 0xfc
],
"r" : [
    #   114 'r'
    0x7c, 0x08, 0x04, 0x04
],
"s" : [
    #   115 's'
    0x48, 0x54, 0x54, 0x24
],
"t" : [
    #   116 't'
    0x04, 0x3f, 0x44, 0x40
],
"u" : [
    #   117 'u'
    0x3c, 0x40, 0x20, 0x7c
],
"v" : [
    #   118 'v'
    0x1c, 0x60, 0x60, 0x1c
],
"w" : [
    #   119 'w'
    0x7c, 0x20, 0x20, 0x7c
],
"x" : [
    #   120 'x'
    0x6c, 0x10, 0x10, 0x6c
],
"y" : [
    #   121 'y'
    0x9c, 0xa0, 0x90, 0x7c
],
"z" : [
    #   122 'z'
    0x44, 0x64, 0x54, 0x4c
],
"{" : [
    #   123 '{' |01234567|
    0x08, #    0|    #   |
    0x36, #    1|  ## ## |
    0x41, #    2| #     #|
    0x00, #    3|        |
],
"|" : [
    #   124 '|' |01234567|
    0x00, #    0|        |
    0x77, #    1| ### ###|
    0x00, #    2|        |
    0x00, #    3|        |
],
"}" : [
    #   125 '}' |01234567|
    0x41, #    0| #     #|
    0x36, #    1|  ## ## |
    0x08, #    2|    #   |
    0x00, #    3|        |
],
"~" : [
    #   126 '~' |01234567|
    0x04, #    0|     #  |
    0x0C, #    1|    ##  |
    0x08, #    2|    #   |
    0x00, #    3|        |
],
":)" : [
    0x28, 0x28, 0x82, 0x7c
]
}
