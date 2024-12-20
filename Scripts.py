from time import sleep
from pygetwindow import getActiveWindow, getAllTitles
from pynput import mouse
from threading import Thread
from pynput.keyboard import KeyCode

import instance
from conf.bindings import AppBindings as AB
from conf.bindings import GameBindings as GB
from conf.bindings import KeyBoard as KB
from conf.config import *
from entity import *
from monitor import *
# from pattern import screenshot

def init():
    instance.input = Input()
    instance.process = GTA()
    instance.weapon = Weapon()
    instance.listener = Listener(on_press,on_release,on_click)

def tab():
    instance.input.press_and_release(GB.Weapons.Weapon_list)



def auto_tab():
    sleep(0.175)
    tab()

def special_press(key1,key2):
    instance.input.press(KeyCode.from_char(key1))
    instance.input.press(KeyCode.from_char(key2))
    instance.input.release(KeyCode.from_char(key2))
    instance.input.release(KeyCode.from_char(key1))
     

def quick_hand():
    special_press(instance.weapon.special_weapon,instance.weapon.hand)

    
def quick_current_weapon():
    if (
        instance.weapon.current == instance.weapon.melee_weapon
        or instance.weapon.current
        == instance.weapon.hand
        or instance.weapon.current
         == instance.weapon.special_weapon
    ):
        instance.weapon.current = instance.weapon.last
    special_press(instance.weapon.special_weapon,instance.weapon.current)


def speed_run():
    while instance.x2_pressed:
        tab()
    quick_current_weapon()


def origin(num):
    return num - 48

def is_in_game():
    if getActiveWindow() != None:
        return GAME_NAME in getActiveWindow().title

def auto_esc():
        instance.input.press_and_release(KB.Esc)
        print('退出')

def buy_ammo():
    instance.input.ahk(GB.Character.Menu, delay=0.2)
    instance.input.ahk(KB.Up, 7)
    instance.input.ahk(KB.Enter, 2)
    instance.input.ahk(KB.Left)
    instance.input.ahk(KB.Down)
    instance.input.ahk(KB.Enter)
    instance.input.ahk(GB.Character.Menu, delay=0)


def wear_necklace():
    instance.input.ahk(GB.Character.Menu, delay=0.2)
    instance.input.ahk(KB.Up, 6)
    instance.input.ahk(KB.Enter)
    instance.input.ahk(KB.Down)
    instance.input.ahk(KB.Enter)
    instance.input.ahk(KB.Down, 6)
    instance.input.ahk(KB.Left)
    instance.input.ahk(GB.Character.Menu, delay=0)


def start_egine():
    instance.input.ahk(GB.Character.Menu, delay=0.2)
    instance.input.ahk(KB.Up, 9)
    instance.input.ahk(KB.Enter)
    instance.input.ahk(KB.Up)
    instance.input.ahk(KB.Enter)
    instance.input.ahk(KB.Down, 2)
    instance.input.ahk(KB.Enter)
    instance.input.ahk(KB.Down, 4)
    instance.input.ahk(KB.Enter, 2)
    instance.input.ahk(GB.Character.Menu, delay=0)


def open_snacks():
    
        instance.input.ahk(GB.Character.Menu, delay=0.2)
        instance.input.ahk(KB.Up, 7)
        instance.input.ahk(KB.Enter)
        instance.input.ahk(KB.Down, 2)
        instance.input.ahk(KB.Enter)


def act3():
        instance.input.press(KB.Down)
        instance.input.press(KB.Right)
        sleep(0.005)
        instance.input.press(KB.Space)
        sleep(0.005)
        instance.input.release(KB.Space)
        instance.input.release(KB.Down)
        instance.input.release(KB.Right)


def right_space():
        instance.input.press(KB.Right)
        sleep(0.005)
        instance.input.press(KB.Space)
        sleep(0.005)
        instance.input.release(KB.Space)
        instance.input.release(KB.Right)


def idle():
        instance.input.press(GB.Character.Look_back)


def kill_game():
       instance.process.kill_process(instance.process.gta5)
       instance.process.kill_process(instance.process.be)
       instance.process.kill_process(instance.process.launcher)
       instance.process.kill_process(instance.process.play_gta5)
       instance.process.kill_process(instance.process.rockstar_service)
       instance.process.kill_process(instance.process.error_handler)
       instance.process.kill_process(instance.process.sc_helper)


def suspend_game():
    if not instance.process.is_suspended(instance.process.gta5):
        instance.process.suspend_process(instance.process.gta5)
        sleep(8)
    instance.process.resume_process(instance.process.gta5)



def auto_reload():  # 自动重启脚本
    print('等待十秒')
    sleep(10)
    print('等待完毕')
    # print(instance.process.Game_Name in getAllTitles())
    while not GAME_NAME in getAllTitles():
        sleep(3)
        print('准备重启中....')
    print('重新初始化')
    instance.process.init_process()
    instance.listener.restart()

def heal():
        print('heal')
        instance.input.press_and_release('c')

def on_click(x, y, button, pressed):
        if is_in_game():
            pass
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
        else:
            pass
            # print(button)
             

def on_press(key):
    if is_in_game():
        try:
            key_v = key.vk
            # print(key.vk)
            if (
                0 <= origin(key_v) <= 9
                and origin(key_v) != instance.weapon.special_weapon
            ):
                auto_tab()
                if (
                    origin(key_v) != instance.weapon.hand
                    and origin(key_v) != instance.weapon.melee_weapon
                ):
                    instance.weapon.current = origin(key_v)
        except AttributeError:
            if key == AB.Buy_Ammo:
                buy_ammo()
            elif key == AB.Wear_Necklace:
                wear_necklace()
            elif key == AB.Start_Engine:
                # start_egine()
                # pascreenshot.main()
                pass
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
    # else:
    #     # print(key)

def on_release(key):
    # if key == AB.Jump:
    #     KeyStatus.Space_Pressed = False
    if key == AB.Instant_Stop:
        # print(instance.img)
        sleep(0.18)
        if Image().perform_template_matching(EXIT,"templates/quit.png"):
            auto_esc()

# def exit_click():
#     AppParmas.Icon.stop()
#     try:
#         instance.listener.Keyboard.stop()
#         instance.listener.Mouse.stop()
#     except Exception as e:
#         print("销毁Listener时发生异常:", e)