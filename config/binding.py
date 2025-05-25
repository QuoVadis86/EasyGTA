# 按键绑定配置文件
from pynput.keyboard import Key
from pynput.mouse import Button


class Game:
    Menu = "m"


class App:

    start_engine = Key.f5
    suspend_gta = Key.end
    kill_gta = Key.delete
    reload_app = Key.f6
    limit_net = Key.f7
    block_net = Key.f8


class KeyBoard:
    Esc = Key.esc
    Space = Key.space
    Up = Key.up
    Down = Key.down
    Left = Key.left
    Right = Key.right
    Enter = Key.enter
    Back = Key.backspace
    Del = Key.delete


class Mouse:

    X1 = Button.x1
    X2 = Button.x2
