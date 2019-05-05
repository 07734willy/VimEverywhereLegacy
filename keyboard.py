from pynput.keyboard import Listener, Controller, Key
from time import sleep

class Keyboard:
    def __init__(self, press_callback, release_callback):
        self.controller = Controller()
        self.press_callback = press_callback
        self.release_callback = release_callback

        self.passthrough_mode = True
        self.modifiers = set()

    # only concerning what vim constitutes as a modifier
    def key_is_modifier(self, key):
        return  key is Key.alt   or key is Key.alt_l   or key is Key.alt_r or \
                key is Key.cmd   or key is Key.cmd_l   or key is Key.cmd_r or \
                key is Key.ctrl  or key is Key.ctrl_l  or key is Key.ctrl_r or \
                key is key.shift or key is Key.shift_l or key is Key.shift_r

    def _on_press(self, key, injected):
        if injected: return

        if self.passthrough_mode:
            self.press_key(key)
            return

        if self.key_is_modifier(key):
            self.modifiers.add(key)
        else: 
            self.press_callback(key, modifiers)

    def _on_release(self, key, injected):
        if injected: return
       
        if self.passthrough_mode:
            self.release_key(key)
            return
        
        if self.key_is_modifier(key):
            self.modifiers.discard(key)
        else: 
            self.release_callback(key, modifiers)

    def press_key(self, key):
        try:
            self.controller.press(key.char)
        except:
            self.controller.press(key)

    def release_key(self, key):
        try:
            self.controller.release(key.char)
        except:
            self.controller.release(key)

    def listen(self):
        with Listener(on_press=self._on_press, on_release=self._on_release, suppress=True) as listener:
            listener.join()

def do_nothing(key, modifiers):
    pass

Keyboard(do_nothing, do_nothing).listen()
