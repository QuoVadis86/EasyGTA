import time
import run
from config.binding import Game as GB
from config.binding import KeyBoard as KB
from config.config import load_config
from pystray import Icon, Menu, MenuItem
from app.tools.utils import format, reload_app


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


def select_unarmed():
    binding = load_config()
    special_weapon = run.listener.get_key(binding.get("special_weapon"))
    unarmed = run.listener.get_key(binding.get("unarmed"))
    run.controller.press(special_weapon)
    run.controller.press(unarmed)
    run.controller.release(unarmed)
    run.controller.release(special_weapon)


def eat_snack():
    binding = load_config()
    eat_snack = run.listener.get_key(binding.get("eat_snack"))
    run.controller.press_and_release(eat_snack)


def press_weapon_wheel():
    binding = load_config()
    weapon_wheel = run.listener.get_key(binding.get("weapon_wheel"))
    run.controller.press_and_release(weapon_wheel)


def hack_speed():
    binding = load_config()
    weapon_wheel = run.listener.get_key(binding.get("weapon_wheel"))
    while run.listener.is_hack_speed:
        print("hack speed")
        run.controller.press_and_release(weapon_wheel)

    special_weapon = run.listener.get_key(binding.get("special_weapon"))
    current_waepon = run.listener.get_key(run.listener.current_weapon)
    run.controller.press(special_weapon)
    run.controller.press(current_waepon)
    run.controller.release(current_waepon)
    run.controller.release(special_weapon)


def suspend_gta():
    run.gta5.suspend()


def kill_gta():
    run.gta5.kill()
    reload_app()


def exit_app():
    run.icon.stop()


def limit_net():
    pass
    # run.gta5.limit_net()


def block_net():
    pass
    # run.gta5.block_net()


def restart():
    run.listener.restart()
    update_app()


def pause():
    run.listener.destroy()


def update_app():
    binding = load_config()
    menu_items = [
        MenuItem(
            "功能",
            Menu(
                MenuItem(f"启动引擎: {format(binding.get('start_engine'))}", None),
                MenuItem(f"断游戏: {format(binding.get('kill_gta'))}", None),
                MenuItem(f"断网: {format(binding.get('block_net'))}", None),
                MenuItem(f"限制网络: {format(binding.get('limit_net'))}", None),
                MenuItem(f"卡单人占据: {format(binding.get('suspend_gta'))}", None),
                MenuItem(
                    f"自动关闭武器选单: {format(binding.get('auto_close'))}", None
                ),
                MenuItem(f"偷速&恢复持枪: {format(binding.get('hack_speed'))}", None),
                MenuItem(f"切空手: {format(binding.get('select_unarmed'))}", None),
            ),
        ),
        MenuItem(
            "武器绑定",
            Menu(
                MenuItem(f"徒手: {format(binding.get('unarmed'))}", None),
                MenuItem(f"近战武器: {format(binding.get('melee'))}", None),
                MenuItem(f"霰弹枪: {format(binding.get('shotgun'))}", None),
                MenuItem(f"重型武器: {format(binding.get('heavy_weapon'))}", None),
                MenuItem(f"特殊武器: {format(binding.get('special_weapon'))}", None),
                MenuItem(f"手枪: {format(binding.get('pistol'))}", None),
                MenuItem(f"冲锋枪: {format(binding.get('smg'))}", None),
                MenuItem(f"突击步枪{format(binding.get('assault_rifle'))}", None),
                MenuItem(f"狙击步枪: {format(binding.get('sniper'))}", None),
                MenuItem(
                    f"武器选单(次要): {format(binding.get('weapon_wheel'))}", None
                ),
                MenuItem(f"吃零食(次要): {format(binding.get('eat_snack'))}", None),
            ),
        ),
        MenuItem("重新加载", restart),
        MenuItem("暂停", pause),
        MenuItem("退出", exit_app),  # 退出不需要阻止关闭
        MenuItem("Creator QuoVadis8", action=None, enabled=False),
    ]
    run.icon.menu = Menu(*menu_items)
