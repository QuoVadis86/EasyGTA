
from time import sleep
from pygetwindow import getActiveWindow, getAllTitles
from Listener import restart as listerner_restart

from ..conf.bindings import GameBindings as GB
from ..conf.config import Names

from .weapon import Weapon
from .input import Input
from .process import GTA5

controller=Input()
gta5=GTA5()

def origin(num):
    return num - 48
def is_in_game():
    if getActiveWindow() != None:
        return Names.GAME_NAME in getActiveWindow().title



def special_press(key):
    press(keyboard.KeyCode.from_char(GameKeyBindings.Weapons.Special_weapon))
    press(keyboard.KeyCode.from_char(key))
    release(keyboard.KeyCode.from_char(key))
    release(keyboard.KeyCode.from_char(GameKeyBindings.Weapons.Special_weapon))



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



