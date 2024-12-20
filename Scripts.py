from time import sleep
from pygetwindow import getActiveWindow, getAllTitles
from pynput import mouse,keyboard
from threading import Thread
from instance import *
import instance
from conf.bindings import AppBindings as AB
from conf.bindings import GameBindings as GB
from conf.bindings import KeyBoard as KB
from conf.config import *
def tab():
    input.press_and_release(weapon.weapon_list)
    print('按下武器选单')


def auto_tab():
    sleep(0.1)
    tab()

def quick_hand():
    input.press(weapon.special_weapon)
    input.press(weapon.hand)
    input.release(weapon.hand)
    input.release(weapon.special_weapon)
    

def quick_current_weapon():
    if (
        weapon.current == weapon.melee_weapon
        or weapon.current
        == weapon.hand
        or weapon.current
         == weapon.special_weapon
    ):
        weapon.current = weapon.last
    input.press(weapon.special_weapon)
    input.press(weapon.current)
    input.release(weapon.current)
    input.release(weapon.special_weapon)


def speed_run():
    while x2_pressed:
        tab()
    quick_current_weapon()


# def continuous_jump():
#             jump()
#             sleep(1)

# def jump():
#     print('跳跃里')
#     inputpress_and_release(GB.Character.Jump)

def origin(num):
    return num - 48
def is_in_game():
    if getActiveWindow() != None:
        return GAME_NAME in getActiveWindow().title
def auto_esc():
        input.press(GB.Character.Franklin)
        print('按下')
        sleep(0.2)
        input.release(GB.Character.Franklin)
        print('弹起')
        input.press_and_release(KB.Esc)
        print('退出')

def buy_ammo():
    input.ahk(GB.Character.Menu, delay=0.2)
    input.ahk(KB.Up, 7)
    input.ahk(KB.Enter, 2)
    input.ahk(KB.Left)
    input.ahk(KB.Down)
    input.ahk(KB.Enter)
    input.ahk(GB.Character.Menu, delay=0)


def wear_necklace():
    input.ahk(GB.Character.Menu, delay=0.2)
    input.ahk(KB.Up, 6)
    input.ahk(KB.Enter)
    input.ahk(KB.Down)
    input.ahk(KB.Enter)
    input.ahk(KB.Down, 6)
    input.ahk(KB.Left)
    input.ahk(GB.Character.Menu, delay=0)


def start_egine():
    input.ahk(GB.Character.Menu, delay=0.2)
    input.ahk(KB.Up, 9)
    input.ahk(KB.Enter)
    input.ahk(KB.Up)
    input.ahk(KB.Enter)
    input.ahk(KB.Down, 2)
    input.ahk(KB.Enter)
    input.ahk(KB.Down, 4)
    input.ahk(KB.Enter, 2)
    input.ahk(GB.Character.Menu, delay=0)


def open_snacks():
    
        input.ahk(GB.Character.Menu, delay=0.2)
        input.ahk(KB.Up, 7)
        input.ahk(KB.Enter)
        input.ahk(KB.Down, 2)
        input.ahk(KB.Enter)


def act3():
        input.press(KB.Down)
        input.press(KB.Right)
        sleep(0.005)
        input.press(KB.Space)
        sleep(0.005)
        input.release(KB.Space)
        input.release(KB.Down)
        input.release(KB.Right)


def right_space():
        input.press(KB.Right)
        sleep(0.005)
        input.press(KB.Space)
        sleep(0.005)
        input.release(KB.Space)
        input.release(KB.Right)


def idle():
        input.press(GB.Character.Look_back)


def kill_game():
       process.kill_process(process.gta5)
       process.kill_process(process.be)
       process.kill_process(process.launcher)
       process.kill_process(process.play_gta5)
       process.kill_process(process.rockstar_service)
       process.kill_process(process.error_handler)
       process.kill_process(process.sc_helper)


def suspend_game():
    if not process.is_suspended(process.gta5):
        # process.resume_process(process.gta5)
        process.suspend_process(process.gta5)
        for _ in range(100):
            if not process.is_suspended(process.gta5):
                break
            sleep(0.08)
    process.resume_process(process.gta5)



def auto_reload():  # 自动重启脚本
    print('等待十秒')
    sleep(10)
    print('等待完毕')
    # print(Process.Game_Name in getAllTitles())
    while not GAME_NAME in getAllTitles():
        sleep(3)
        print('准备重启中....')
    print('重新初始化')
    process.init_process()
    listener.restart()

def heal():
        print('heal')
        input.press_and_release('c')

def on_click(x, y, button, pressed):
        if is_in_game():
            if pressed:
                if button == mouse.Button.x1:
                    Thread(target=quick_hand).start()
                elif button == mouse.Button.x2:
                    instance.x2_pressed = True
                    Thread(target=speed_run).start()
                else:
                    pass
            else:
                if button == mouse.Button.x2:
                    instance.x2_pressed = False
                if button == mouse.Button.left:
                    instance.left_pressed = False


def on_press(key):
    if is_in_game():
        try:
            key_v = key.vk
            if (
                0 <= origin(key_v) <= 9
                and origin(key_v) != weapon.special_weapon
            ):
                auto_tab()
                if (
                    origin(key_v) != weapon.hand
                    and origin(key_v) != weapon.melee_weapon
                ):
                    weapon.current = origin(key_v)
        except AttributeError:
            if key == AB.Buy_Ammo:
                buy_ammo()
            elif key == AB.Wear_Necklace:
                wear_necklace()
            elif key == AB.Start_Engine:
                start_egine()
            elif key == AB.Open_Snacks:
                open_snacks()
            elif key == AB.Idle:
                idle()
            # elif key == AB.Jump:
            #     if not instance.space_pressed:
            #         Thread(target=continuous_jump).start()
            # elif key == AB.Heal:
            #     if not KeyStatus.Tab_Pressed:
            #         Thread(target=heal).start()
            elif key == AB.Suspend:
                Thread(target=suspend_game).start()
            elif key == AB.Kill:
                Thread(target=kill_game).start()
    else:
            print(key)
            pass
            # if key == AB.Heal:
            #     heal()
            # elif key == AB.Buy_Ammo:
            #     buy_ammo()
            # elif key == AB.Wear_Necklace:
            #     wear_necklace()
            # elif key == AB.Start_Engine:
            #     start_egine()
            # elif key == AB.Open_Snacks:
            #     open_snacks()
            # elif key == AB.Idle:
            #     idle()
            # elif key == AB.Jump:
            #     if not KeyStatus.Space_Pressed:
            #         Thread(target=continuous_jump).start()
            # elif key == AB.Heal:
            #     if not KeyStatus.Tab_Pressed:
            #         Thread(target=heal).start()
            # elif key == AB.Suspend:
            #     GameParmas.Is_Suspend = not GameParmas.Is_Suspend
            #     Thread(target=suspend_game).start()
            # elif key == AB.Kill:
                # Thread(target=kill_game).start()
def on_release(key):
    # if key == AB.Jump:
    #     KeyStatus.Space_Pressed = False
    if key == AB.Instant_Stop:
        auto_esc()

# def exit_click():
#     AppParmas.Icon.stop()
#     try:
#         Listener.Keyboard.stop()
#         Listener.Mouse.stop()
#     except Exception as e:
#         print("销毁Listener时发生异常:", e)