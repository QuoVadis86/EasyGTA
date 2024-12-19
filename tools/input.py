from time import sleep
from Config import Process, Listener,AppParmas
from pygetwindow import getActiveWindow, getAllTitles
from KeyBindings import GameKeyBindings
from Listener import restart as listerner_restart
from tools.process import (
    suspend_process,
    kill_process,
    resume_process,
    pid_init
)
from pynput import keyboard, mouse
class Input():
    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        # self.
        # pass
    def press_and_release(self,key):
        self.keyboard.press(key)
        self.keyboard.release(key)
    def press(self,key):
        self.keyboard.press(key)

    def release(self,key):
        self.keyboard.release(key)








def ahk(key, times=1, delay=0.02):
    for i in range(times):
        press_and_release(key)
    sleep(delay)


def restart():
    listerner_restart()


def exit_click():
    AppParmas.Icon.stop()
    try:
        Listener.Keyboard.stop()
        Listener.Mouse.stop()
    except Exception as e:
        print("销毁Listener时发生异常:", e)

def auto_reload():  # 自动重启脚本
    print('等待十秒')
    sleep(10)
    print('等待完毕')
    # print(Process.Game_Name in getAllTitles())
    while not Process.Game_Name in getAllTitles():
        sleep(3)
        print('准备重启中....')
    print('重新初始化内存')
    pid_init()
    restart()
    


def block():

    print("blcok")


def unblock():
    print("restore")



