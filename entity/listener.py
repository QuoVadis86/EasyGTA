from pynput import keyboard, mouse

    
class Listener():
    def __init__(self,on_press,on_release,on_click):
        print('初始化监听器')
        self.on_press=on_press
        self.on_release=on_release
        self.on_click=on_click
        self.initialize_listeners()

    def initialize_listeners(self):
        self.key_listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.start()

    def start(self):
        self.key_listener.start()
        self.mouse_listener.start()
        self.key_listener.join()
        self.mouse_listener.join()
 

    def destroy(self):
        self.key_listener.stop()
        self.mouse_listener.stop()

    def restart(self):
        self.destroy()
        self.initialize_listeners()
        self.start()
    