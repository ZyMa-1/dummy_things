from typing import Any


class Colored:
    color_dict = {
        "yellow": "\033[1;33m",
        "red": "\033[1;31m",
        "blue": "\033[1;34m",
        "reset": "\033[00m"
    }

    def __init__(self, obj: Any, color: str, *, is_percentage=False):
        self.obj = obj
        self.prefix = self.color_dict[color]
        self.suffix = self.color_dict['reset']
        self.is_percentage = is_percentage
        if is_percentage:
            self.str = self.prefix + str(self.obj) + "%" + self.suffix
        else:
            self.str = self.prefix + str(self.obj) + self.suffix

    def __float__(self):
        try:
            return float(self.obj)
        except ValueError:
            return None

    def __int__(self):
        try:
            return int(self.obj)
        except ValueError:
            return None

    def __repr__(self):
        return self.str

    def __str__(self):
        return self.str

    def __format__(self, format_spec):
        return self.prefix + format(self.obj, format_spec) + ("%" if self.is_percentage else "") + self.suffix
