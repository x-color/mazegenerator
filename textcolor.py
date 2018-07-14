class TextColor:
    COLOR = {
        'clear': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'invisible': '\033[08m',
        'reverse': '\033[07m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bg_black': '\033[40m',
        'bg_red': '\033[41m',
        'bg_green': '\033[42m',
        'bg_yellow': '\033[43m',
        'bg_blue': '\033[44m',
        'bg_purple': '\033[45m',
        'bg_cyan': '\033[46m',
        'bg_white': '\033[47m',
    }

    @classmethod
    def _paint(cls, text, color):
        painted_text = color + text + cls.COLOR['clear']
        return painted_text

    @classmethod
    def black(cls, text, backgroud=False):
        if backgroud:
            return cls._paint(text, cls.COLOR['bg_black'])
        else:
            return cls._paint(text, cls.COLOR['black'])

    @classmethod
    def red(cls, text, backgroud=False):
        if backgroud:
            return cls._paint(text, cls.COLOR['bg_red'])
        else:
            return cls._paint(text, cls.COLOR['red'])

    @classmethod
    def green(cls, text, backgroud=False):
        if backgroud:
            return cls._paint(text, cls.COLOR['bg_green'])
        else:
            return cls._paint(text, cls.COLOR['green'])

    @classmethod
    def yellow(cls, text, backgroud=False):
        if backgroud:
            return cls._paint(text, cls.COLOR['bg_yellow'])
        else:
            return cls._paint(text, cls.COLOR['yellow'])

    @classmethod
    def blue(cls, text, backgroud=False):
        if backgroud:
            return cls._paint(text, cls.COLOR['bg_blue'])
        else:
            return cls._paint(text, cls.COLOR['blue'])

    @classmethod
    def purple(cls, text, backgroud=False):
        if backgroud:
            return cls._paint(text, cls.COLOR['bg_purple'])
        else:
            return cls._paint(text, cls.COLOR['purple'])

    @classmethod
    def cyan(cls, text, backgroud=False):
        if backgroud:
            return cls._paint(text, cls.COLOR['bg_cyan'])
        else:
            return cls._paint(text, cls.COLOR['cyan'])

    @classmethod
    def white(cls, text, backgroud=False):
        if backgroud:
            return cls._paint(text, cls.COLOR['bg_white'])
        else:
            return cls._paint(text, cls.COLOR['white'])

    @classmethod
    def bold(cls, text):
        return cls._paint(text, cls.COLOR['bold'])

    @classmethod
    def underline(cls, text):
        return cls._paint(text, cls.COLOR['underline'])

    @classmethod
    def invisible(cls, text):
        return cls._paint(text, cls.COLOR['invisible'])

    @classmethod
    def reverse(cls, text):
        return cls._paint(text, cls.COLOR['reverse'])
