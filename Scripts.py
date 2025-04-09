
import run
from conf.binding import Game as GB
from conf.binding import KeyBoard as KB
from conf.binding import App as AB
from conf.config import load_config
from pystray import Icon, Menu, MenuItem
from app.tools.utils import format
def start_egine():
    run.controller.ahk(GB.Menu, delay=0.2)
    run.controller.ahk(KB.Up, 9)
    run.controller.ahk(KB.Enter)
    run.controller.ahk(KB.Up)
    run.controller.ahk(KB.Enter)
    run.controller.ahk(KB.Down, 2)
    run.controller.ahk(KB.Enter)
    run.controller.ahk(KB.Down, 4)
    run.controller.ahk(KB.Enter, 2)
    run.controller.ahk(GB.Menu, delay=0)

def suspend_gta():
    run.gta5.suspend()
def kill_gta():
    run.gta5.kill()
def exit_app():
    run.icon.stop()
def limit_net():
    run.gta5.limit_net()
def block_net():
    run.gta5.block_net()

def restart():
    run.listener.restart()
    update_app()

    # run.icon.stop()
    # run.icon.run()
   

def pause():
    run.listener.destroy()
    

# def format(key):
#     return str(key).split(".")[-1].capitalize()
    
def update_app():
    binding=load_config()
    menu_items = [
        MenuItem(
            "功能",
            Menu(
                MenuItem(f"启动引擎: {format(binding.get('start_engine'))}", None),
                MenuItem(f"断游戏: {format(binding.get('kill_gta'))}", None),
                MenuItem(f"断网: {format(binding.get('block_net'))}", None),
                MenuItem(f"限制网络: {format(binding.get('limit_net'))}", None),
                MenuItem(f"卡单人占据: {format(binding.get('suspend_gta'))}", None),
            ),
        ),
        MenuItem("重新加载", restart),
        MenuItem("暂停", pause),
        MenuItem("退出", exit_app),  # 退出不需要阻止关闭
        MenuItem("Creator QuoVadis8", action=None, enabled=False),
    ]
    run.icon.menu = Menu(*menu_items)