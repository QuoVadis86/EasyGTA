from threading import Thread
from time import sleep
from pynput import keyboard, mouse
import logging
from scripts import start_egine,exit_app
from conf.binding import App as AB, KeyBoard as KB,Mouse as MB
class Controller():
    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        logging.info("初始化输入控制器")


    def press(self, key):
        self.keyboard.press(key)

    def release(self, key):
        self.keyboard.release(key)

    def press_and_release(self, key, delay: float = 0):
        self.keyboard.press(key)
        sleep(delay)
        self.keyboard.release(key)
    
    def ahk(self, key, times: int = 1, delay: float = 0):
        for _ in range(times):
            self.press_and_release(key)
            sleep(delay)
    

    
class Listener():
    def __init__(self):
        self.initializes()
        logging.info("初始化监听器")
       
    def initializes(self):
        self.keyboard= keyboard.Listener(on_press=on_press)
        self.mouse= mouse.Listener(on_click=on_click)



    def start(self):
        self.keyboard.start()
        self.mouse.start()
        logging.info("监听器已启动")
        # self.keyboard.join()
        # self.mouse.join()
 

    def destroy(self):
        self.keyboard.stop()
        self.mouse.stop()
        logging.info("监听器已销毁")

    def restart(self):
        self.destroy()
        self.initializes()
        self.start()

def on_click(x, y, button, pressed):
        # if game_focused():
            if pressed:
                if button ==AB.Start_Engine:
                    Thread(target=start_egine).start()
                else:
                    pass
        # else:
            # pass
            # print(button)
             

def on_press(key):
    
    # if game_focused():
        try:
            key_v = key.vk
            # print(key.vk)
            print(key)
            
        except AttributeError:
            print(key)
            if key == AB.Start_Engine:
              start_egine()
            if key==KB.Del:
                exit_app()
                 
    # else:
    #     # print(key)


if __name__ == "__main__":
    # Listener()
    pass
