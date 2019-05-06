from keyboard import Keyboard

def on_press(key, modifiers):
    vim_talker.send_key(key, modifiers)

def run():
    keyboard = Keyboard(on_press, None)
    keyboard.listen()

if __name__ == "__main__":
    on_press = None
    run()
else:
    import vim_talker
