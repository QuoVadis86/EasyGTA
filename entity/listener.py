from pynput import keyboard, mouse
from threading import Thread

from scripts import *
from conf.bindings import AppBindings as AB
from scripts import on_click
from scripts import on_press
from scripts import on_release
class Listener:
    def __init__(self):
        print('初始化监听器')
        self.initialize_listeners()

    def initialize_listeners(self):
        self.key_listener = keyboard.Listener(on_press=on_press,on_release=on_release)
        self.mouse_listener = mouse.Listener(on_click=on_click)

    def start(self):
        self.key_listener.start()
        self.mouse_listener.start()

    def destroy(self):
        self.key_listener.stop()
        self.mouse_listener.stop()

    def restart(self):
        self.destroy()
        self.initialize_listeners()
        self.start()
    