


class ColorCode:
    """
    IRC colors codes, as ints.
    For simple use, you should use Color object.
    """
    White     =  0
    Black     =  1
    DarkBlue  =  2
    DarkGreen =  3
    Red       =  4
    Brown     =  5
    Purple    =  6
    Orange    =  7
    Yellow    =  8
    Green     =  9
    Cyan      = 10
    LightCyan = 11
    Blue      = 12
    Pink      = 13
    Gray      = 14
    LightGray = 15

class ControlCode:
    """
    IRC control codes, as ints.
    For simple use, you should use Control object.
    """
    Bold          =  2  # 0x02
    Color         =  3  # 0x03
    Italic        =  9  # 0x09
    StrikeThrough = 19  # 0x13
    Reset         = 15  # 0x0f
    Underline     = 21  # 0x15
    Underline2    = 31  # 0x1f
    Reverse       = 22  # 0x16

class _Color:
    def __dir__(self):
        return [a for a in dir(ColorCode) if a[0] != '_']

    def __getattr__(self, color):
        if hasattr(ColorCode, color):
            return '%c%d' % (ControlCode.Color, getattr(ColorCode, color))
        else:
            raise AttributeError(color)

"IRC color codes, as strings."
Color = _Color()

class _Control:
    def __dir__(self):
        return [a for a in dir(ControlCode) if a[0] != '_']

    def __getattr__(self, control):
        if hasattr(ControlCode, control):
            return '%c' % (getattr(ControlCode, control),)
        else:
            raise AttributeError(control)

"IRC control codes, as strings."
Control = _Control()
