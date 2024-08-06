from pynput import keyboard
from pynput.keyboard import Key

class UserInput:
    def __init__(self) -> None:
        self.name = "Hello"

    def on_key_release(self, key):
        if key == Key.right:
            print("Right Key pressed")
            return 'r'
        elif key == Key.left:
            print("Left Key pressed")
            return 'l'
        elif key == Key.up:
            print("Up Key pressed")
            return 'u'
        elif key == Key.down:
            print("Down Key pressed")
            return 'd'
        elif key == Key.esc:
            exit()
    
    def get_user_input(self) -> str:
        with keyboard.Listener(on_release=self.on_key_release) as listener:
            listener.join()