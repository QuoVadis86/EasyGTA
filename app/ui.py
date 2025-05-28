import os
import sys
from threading import Thread
from pystray import Icon, Menu, MenuItem
import run
from PIL import Image
from config import config
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
                MenuItem(f"自动关闭武器选单: {format(binding.get('auto_close'))}", None),
                MenuItem(f"偷速&恢复持枪: {format(binding.get('hack_speed'))}", None),
                MenuItem(f"切空手: {format(binding.get('select_unarmed'))}", None),

            ),
        ),
        MenuItem("武器绑定",
            Menu(
                MenuItem(f"徒手: {format(binding.get('unarmed'))}", None),
                MenuItem(f"近战武器: {format(binding.get('melee'))}", None),
                MenuItem(f"霰弹枪: {format(binding.get('shotgun'))}", None),
                MenuItem(f"重型武器: {format(binding.get('heavy_weapon'))}", None),
                MenuItem(f"特殊武器: {format(binding.get('special_weapon'))}", None),
                MenuItem(f"手枪: {format(binding.get('pistol'))}", None),
                MenuItem(f"冲锋枪: {format(binding.get('smg'))}", None),
                MenuItem(f":突击步枪{format(binding.get('assault_rifle'))}", None),
                MenuItem(f"狙击步枪: {format(binding.get('sniper'))}", None),
                MenuItem(f"武器选单(次要): {format(binding.get('weapon_wheel'))}", None),
                MenuItem(f"吃零食(次要): {format(binding.get('eat_snack'))}", None),

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
