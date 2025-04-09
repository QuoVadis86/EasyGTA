import os
import sys
from threading import Thread
from pystray import Icon, Menu, MenuItem
import run
from PIL import Image
from conf import config
from scripts import restart, exit_app, pause,format

binding = config.load_config()






def get_resource_path(relative_path):
    """获取资源文件的绝对路径"""
    try:
        # 打包后的路径
        base_path = sys._MEIPASS
    except Exception:
        # 开发环境路径
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def create_ui():
    icon_path = get_resource_path("png/icon.png")
    icon_image = Image.open(icon_path)

    # 修改所有回调函数，确保都返回False
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

    menu = Menu(*menu_items)
    run.icon = Icon(
        "Easy GTA5", icon_image, menu=menu, title="Created By QuoVadis8 For GTA5"
    )
    run.icon.run()
