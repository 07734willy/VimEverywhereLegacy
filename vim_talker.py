import vim
from pynput.keyboard import Key, KeyCode

class VimKeyError(Exception): pass


def vimify_modifiers(modifiers):
    alt_keys   = (Key.alt,   Key.alt_l,   Key.alt_r)
    cmd_keys   = (Key.cmd,   Key.cmd_l,   Key.cmd_r)
    ctrl_keys  = (Key.ctrl,  Key.ctrl_l,  Key.ctrl_r)
    shift_keys = (Key.shift, Key.shift_l, Key.shift_r)

    mappings = { alt_keys : "M-",
                 cmd_keys : "D-",
                ctrl_keys : "C-",
               shift_keys : "S-" }

    out = ""
    for keys, prefix in mappings.items():
        if any(key in modifiers for key in keys):
            out += prefix
    return out

def vimify_special(key):
    map = { Key.backspace : "BS",
            Key.delete    : "Del",
            Key.down      : "Down",
            Key.end       : "End",
            Key.enter     : "Enter",
            Key.esc       : "Esc",
            
            Key.f1  : "F1",
            Key.f2  : "F2",
            Key.f3  : "F3",
            Key.f4  : "F4",
            Key.f5  : "F5",
            Key.f6  : "F6",
            Key.f7  : "F7",
            Key.f8  : "F8",
            Key.f9  : "F9",
            Key.f10 : "F10",
            Key.f11 : "F11",
            Key.f12 : "F12",

            Key.home      : "Home",
            Key.left      : "Left",
            Key.page_down : "PageDown",
            Key.page_up   : "PageUp",
            Key.right     : "Right",

            Key.space   : "Space",
            Key.tab     : "Tab",
            Key.up      : "Up",
            Key.insert  : "Insert" }

    if key not in map:
        raise VimKeyError("Special key not supported by vim")
    
    return map[key]

def enter_normal_mode():
    send_key(Key.esc)

def clear_buffer():
    vim.command("%d_")

def get_buffer():
    return "\n".join(vim.current.buffer)

def to_vim_format(key, modifiers):
    try:
        key_str = key.char
        # return the literal character without `< >`s if no modifiers nor special keys
        if not modifiers:
            return key_str
    except:
        # Throws exception if key still is not found
        key_str = vimify_special(key)
   
    modifier_str = vimify_modifiers(modifiers)
    return "\\<{}{}>".format(modifier_str, key_str)

def send_key(key, modifiers=set()):
    try:
        vim_key = to_vim_format(key, modifiers)
        vim.command("call feedkeys(\"{}\", 't')".format(vim_key))
        #print("call feedkeys(\"{}\", 't')".format(vim_key))
    except VimKeyError:
        pass

