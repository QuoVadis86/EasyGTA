
from time import sleep
from Config import Process, Listener,AppParmas
from pygetwindow import getActiveWindow, getAllTitles
from conf.key_bindings import GameKeyBindings
from Listener import restart as listerner_restart
from .process import pid_init

from pynput import keyboard, mouse

def init():
    Listener.Keyboard_Controller = keyboard.Controller()
    Listener.Mouse_Controller = mouse.Controller()

def set_current_weapon(weapon):
    GameKeyBindings.Weapons.Current_Weapon=weapon
def current_weapon():
    return GameKeyBindings.Weapons.Current_Weapon

def set_last_weapon(weapon):
    GameKeyBindings.Weapons.Last_Weapon=weapon
def last_weapon():
    return GameKeyBindings.Weapons.Last_Weapon


def origin(num):
    return num - 48


def is_in_game():
    if getActiveWindow() != None:
        return Process.Game_Name in getActiveWindow().title


def press_and_release(key):
    Listener.Keyboard_Controller.press(key)
    Listener.Keyboard_Controller.release(key)

def special_press(key):
    press(keyboard.KeyCode.from_char(GameKeyBindings.Weapons.Special_weapon))
    press(keyboard.KeyCode.from_char(key))
    release(keyboard.KeyCode.from_char(key))
    release(keyboard.KeyCode.from_char(GameKeyBindings.Weapons.Special_weapon))

def press(key):
    Listener.Keyboard_Controller.press(key)


def release(key):
    Listener.Keyboard_Controller.release(key)


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



