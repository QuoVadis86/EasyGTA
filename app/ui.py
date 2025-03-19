from threading import Thread
from pystray import Icon, Menu, MenuItem
import run
from PIL import Image

# # 假设这些函数来自外部模块
# from tools.utils import restart_listener
from scripts import restart, exit_app
# from conf.Config import AppParmas



# 更新 BadSportValue 菜单项的回调函数
def test():
    global value
    value += 1
    print(value)
    # 重新创建菜单项
    menu = Menu(
        # MenuItem(f"测试 : {value} (点击刷新)", test),
        MenuItem("重新加载", restart),
        MenuItem("退出", exit_app)
    )
    run.icon.menu = menu


# 创建托盘图标和菜单项
def create_ui():
    icon_image = Image.open("png/icon.png")

    # 初始菜单项
    menu_items = [
        # MenuItem(f"测试 : {value} (点击刷新)", test),
        MenuItem("重新加载", restart),
        MenuItem("退出", exit_app)
    ]

    menu = Menu(*menu_items)
    run.icon = Icon(
        "Easy GTA5", icon_image, menu=menu, title="Created By QuoVadis8 For GTA5")

    run.icon.run()

def init():
    Thread(target=create_ui).start()
