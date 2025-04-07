from threading import Thread
from pystray import Icon, Menu, MenuItem
import run
from PIL import Image
from conf import binding,config
from scripts import restart, exit_app, pause

def update_key(key, value):
    print(key, value)
    menu_items = [
        MenuItem("功能", Menu(
            MenuItem(f"启动引擎1: {format(binding.App.Start_Engine)}", 
                   lambda: (update_key("start_engine", 1) or False)),
            MenuItem(f"断游戏2: {format(binding.App.Kill)}", 
                   lambda: (update_key("del", 1) or False)),
            MenuItem(f"限制网络3: {format(binding.App.Net_Limit)}", 
                   lambda: (update_key("limit", 1) or False)),
            MenuItem(f"卡单人占据4: {format(binding.App.Suspend)}",
                   lambda: (update_key("singlee", 1) or False)),
        )),
        MenuItem("重新加载", restart), 
        MenuItem("暂停",pause),   
        MenuItem("退出", exit_app),  # 退出不需要阻止关闭
        MenuItem("Creator QuoVadis8", action=None, enabled=False),
    ]
    run.icon.menu = Menu(*menu_items)

def format(key):
    return str(key).split(".")[-1].capitalize()

def create_ui():
    icon_image = Image.open("png/icon.png")

    # 修改所有回调函数，确保都返回False
    menu_items = [
        MenuItem("功能", Menu(
            MenuItem(f"启动引擎: {format(binding.App.Start_Engine)}", 
                   lambda: (update_key("start_engine", 1) or False)),
            MenuItem(f"断游戏: {format(binding.App.Kill)}", 
                   lambda: (update_key("del", 1) or False)),
            MenuItem(f"限制网络: {format(binding.App.Net_Limit)}", 
                   lambda: (update_key("limit", 1) or False)),
            MenuItem(f"卡单人占据: {format(binding.App.Suspend)}",
                   lambda: (update_key("singlee", 1) or False)),
        )),
        MenuItem("重新加载", restart), 
        MenuItem("暂停",pause),   
        MenuItem("退出", exit_app),  # 退出不需要阻止关闭
        MenuItem("Creator QuoVadis8", action=None, enabled=False),
    ]

    menu = Menu(*menu_items)
    run.icon = Icon(
        "Easy GTA5", icon_image, menu=menu, title="Created By QuoVadis8 For GTA5")
    print(config.get_external_config_path())
    run.icon.run()