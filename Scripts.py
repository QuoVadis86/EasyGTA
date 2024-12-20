from time import sleep
import tools.Utils as Utils
from conf.bindings import GameKeyBindings, KeyBoard
from conf.Config import GameParmas, KeyStatus

def tab():
    Utils.press_and_release(GameKeyBindings.Weapons.Weapon_list)
    print('按下tab')


def auto_tab():
    sleep(0.1)
    tab()


def hand():
    Utils.special_press(GameKeyBindings.Weapons.Hand)


def quick_current_weapon():
    if (
        GameKeyBindings.Weapons.Current_Weapon == GameKeyBindings.Weapons.Melee_weapon
        or GameKeyBindings.Weapons.Current_Weapon
        == GameKeyBindings.Weapons.Hand
        or GameKeyBindings.Weapons.Current_Weapon
         == GameKeyBindings.Weapons.Special_weapon
    ):
        GameKeyBindings.Weapons.Current_Weapon = GameKeyBindings.Weapons.Last_Weapon
    Utils.special_press(GameKeyBindings.Weapons.Current_Weapon)


def speed_run():
    while KeyStatus.X2_Pressed:
        tab()
    quick_current_weapon()


def continuous_jump():
            jump()
            sleep(1)

def jump():
    print('跳跃里')
    Utils.press_and_release(GameKeyBindings.Character.Jump)


def auto_esc():
        Utils.press(GameKeyBindings.Character.Franklin)
        print('按下')
        sleep(0.2)
        Utils.release(GameKeyBindings.Character.Franklin)
        print('弹起')
        Utils.press_and_release(KeyBoard.Esc)
        print('退出')

def buy_ammo():
    Utils.ahk(GameKeyBindings.Character.Menu, delay=0.2)
    Utils.ahk(KeyBoard.Up, 7)
    Utils.ahk(KeyBoard.Enter, 2)
    Utils.ahk(KeyBoard.Left)
    Utils.ahk(KeyBoard.Down)
    Utils.ahk(KeyBoard.Enter)
    Utils.ahk(GameKeyBindings.Character.Menu, delay=0)


def wear_necklace():
    Utils.ahk(GameKeyBindings.Character.Menu, delay=0.2)
    Utils.ahk(KeyBoard.Up, 6)
    Utils.ahk(KeyBoard.Enter)
    Utils.ahk(KeyBoard.Down)
    Utils.ahk(KeyBoard.Enter)
    Utils.ahk(KeyBoard.Down, 6)
    Utils.ahk(KeyBoard.Left)
    Utils.ahk(GameKeyBindings.Character.Menu, delay=0)


def start_egine():
    Utils.ahk(GameKeyBindings.Character.Menu, delay=0.2)
    Utils.ahk(KeyBoard.Up, 9)
    Utils.ahk(KeyBoard.Enter)
    Utils.ahk(KeyBoard.Up)
    Utils.ahk(KeyBoard.Enter)
    Utils.ahk(KeyBoard.Down, 2)
    Utils.ahk(KeyBoard.Enter)
    Utils.ahk(KeyBoard.Down, 4)
    Utils.ahk(KeyBoard.Enter, 2)
    Utils.ahk(GameKeyBindings.Character.Menu, delay=0)


def open_snacks():
    
        Utils.ahk(GameKeyBindings.Character.Menu, delay=0.2)
        Utils.ahk(KeyBoard.Up, 7)
        Utils.ahk(KeyBoard.Enter)
        Utils.ahk(KeyBoard.Down, 2)
        Utils.ahk(KeyBoard.Enter)


def act3():
        Utils.press(KeyBoard.Down)
        Utils.press(KeyBoard.Right)
        sleep(0.005)
        Utils.press(KeyBoard.Space)
        sleep(0.005)
        Utils.release(KeyBoard.Space)
        Utils.release(KeyBoard.Down)
        Utils.release(KeyBoard.Right)


def right_space():
        Utils.press(KeyBoard.Right)
        sleep(0.005)
        Utils.press(KeyBoard.Space)
        sleep(0.005)
        Utils.release(KeyBoard.Space)
        Utils.release(KeyBoard.Right)


def idle():
        Utils.press(GameKeyBindings.Character.Look_back)


def kill_game():
       Utils.kill()
       Utils.auto_reload()


def suspend_game():
    if GameParmas.Is_Suspend:
        Utils.suspend()
        for i in range(100):
            if GameParmas.Is_Suspend:
                sleep(0.08)
            else:
                break
        Utils.resume()
        GameParmas.Is_Suspend = False


def heal():
        print('heal')
        Utils.press_and_release('c')