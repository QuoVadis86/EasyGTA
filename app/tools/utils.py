import run
from pygetwindow import getActiveWindow, getAllTitles
from config.config import GAME_NAME_LEGACY,GAME_NAME_ENHANCED
from time import sleep


def game_focused():
    if getActiveWindow() != None:
        print("当前激活的窗口标题是：",getActiveWindow().title)
        return GAME_NAME_ENHANCED in getActiveWindow().title or GAME_NAME_LEGACY in getActiveWindow().title or GAME_NAME_ENHANCED in getActiveWindow().title

def reload_app():  # 自动重启脚本
    print("等待十秒")
    sleep(10)
    print("等待完毕")
    # print(instance.process.Game_Name in getAllTitles())
    while not GAME_NAME_LEGACY in getAllTitles() or not GAME_NAME_ENHANCED in getAllTitles():
        sleep(3)
        print("准备重启中....")
    print("重新初始化")
    run.gta5.init_process()
    run.listener.restart()


def restart_listener():
    run.listener.restart()


def format(key):
    if not key:
        return
    return str(key).split(".")[-1].capitalize()
