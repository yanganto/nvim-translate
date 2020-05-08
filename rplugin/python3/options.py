from enum import Enum

class DisplayType(Enum):
    STATUS = 0
    POPUP = 1

class CTERMColorsEnum(Enum):
    """ Return a validate color else black as fallback """
    @classmethod
    def from_str(klass, color):
        color_name = color.upper()
        if color_name in ("BLACK", "DARKBLUE", "DARKGREEN", "DARKCYAN", "DARKRED", "DARKMAGENTA",
                          "BROWN", "GREY", "DARKGREY", "BLUE", "GREEN", "CYAN", "RED", "MAGENTA",
                          "YELLOW", "WHITE"):
            return klass[color_name]
        else:
            return klass(0)

class CTERMColors(CTERMColorsEnum):
    BLACK = 0
    DARKBLUE = 1
    DARKGREEN = 2
    DARKCYAN = 3
    DARKRED = 4
    DARKMAGENTA = 5
    BROWN = 6
    GREY = 7
    DARKGREY = 8

    BLUE = 9
    GREEN = 10
    CYAN = 11
    RED = 12
    MAGENTA = 13
    YELLOW = 14
    WHITE = 15

class CTERMColors_8(CTERMColorsEnum):
    BLACK = 0
    DARKBLUE = 1
    DARKGREEN = 2
    DARKCYAN = 3
    DARKRED = 4
    DARKMAGENTA = 5
    BROWN = 6
    GREY = 7
    DARKGREY = 8

    RED = 9
    GREEN = 10
    YELLOW = 11
    BLUE = 12
    MAGENTA = 13
    CYAN = 14
    WHITE = 15

