
import run
from pygetwindow import getActiveWindow, getAllTitles
from conf.config import GAME_NAME
from time import sleep

def game_focused():
    if getActiveWindow() != None:
        return GAME_NAME in getActiveWindow().title
    
def reload_app():  # 自动重启脚本
    print('等待十秒')
    sleep(10)
    print('等待完毕')
    # print(instance.process.Game_Name in getAllTitles())
    while not GAME_NAME in getAllTitles():
        sleep(3)
        print('准备重启中....')
    print('重新初始化')
    run.gta5.init_process()
    run.listener.restart()

def restart_listener():
    run.listener.restart()


def format(key):
    return str(key).split(".")[-1].capitalize()

