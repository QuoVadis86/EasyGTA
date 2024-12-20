from time import sleep
from pynput import keyboard, mouse


class Input:
    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()

    def press_and_release(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def press(self, key):
        self.keyboard.press(key)

    def release(self, key):
        self.keyboard.release(key)

    def ahk(self, key, times: int = 1, delay: float = 0):
        for i in range(times):
            self.press_and_release(key)
            sleep(delay)
