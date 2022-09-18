

hid_codes = ['', '', '', '', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', '0', 'enter', 'esc', 'backspace', 'tab', 'space', '-', '=', '[',
             ']', '\\', '...', ';', '\'', '`', ',', '.', '/', 'capslock', 'f1', 'f2',
             'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'prtscr', 'scrolllock',
             'pause', 'insert', 'home', 'pageup', 'del', 'end', 'pageup', 'right', 'left', 'down', 'up', 'numlock',
             'divide', 'multiply', 'subtract', 'add', 'numpadenter', 'numpad1', 'numpad2', 'numpad3', 'numpad4', 'numpad5', 'numpad6', 'numpad7',
             'numpad8', 'numpad9', 'numpad0', 'decimal', '...', 'applic', 'power', 'numpad=', 'f13', 'f14', 'f15', 'f16',
             'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'execute', 'help', 'menu', 'select',
             'stop', 'again', 'undo', 'cut', 'copy', 'paste', 'find', 'mute', 'volume up', 'volume down', 'locking caps lock', 'locking num lock',
             'locking scroll lock', 'numpad,', 'numpad=', 'internat', 'internat', 'internat', 'internat', 'internat', 'internat', 'internat', 'internat', 'internat',
             'lang', 'lang', 'lang', 'lang', 'lang', 'lang', 'lang', 'lang', 'lang', 'alt erase', 'sysrq', 'cancel',
             'clear', 'prior', 'return', 'separ', 'out', 'oper', 'clear', 'crsel', 'exsel']

hid_mods = ['ctrlleft', 'shiftleft', 'altleft',
            'winleft', 'ctrlright', 'shiftright', 'altright', 'winright']


def hid_code_to_string(code):
    if code >= 224:
        print(code)
        return hid_mods[code - 224]
    return hid_codes[code]


def string_to_hid_code(string):
    try:
        return hid_codes.index(string)
    except:
        return hid_mods.index(string) + 224
