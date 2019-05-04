from pynput import keyboard
from time import sleep


def on_press(key, inject):
    if inject: return
    #print("Pressed: {}".format(key))
    press_key(key)

def on_release(key, inject):
    if inject: return
    #print("Released: {}".format(key))
    release_key(key)

def press_key(key):
    try:
        controller.press(key.char)
    except:
        controller.press(key)

def release_key(key):
    try:
        controller.release(key.char)
    except:
        controller.release(key)

controller = keyboard.Controller()

with keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True) as listener:
    listener.join()

