from threading import Thread
from run import controller
from conf.binding import Game as GB
from conf.binding import KeyBoard as KB
from conf.binding import App as AB
from conf.config import *


def start_egine():
    controller.ahk(GB.Menu, delay=0.2)
    controller.ahk(KB.Up, 9)
    controller.ahk(KB.Enter)
    controller.ahk(KB.Up)
    controller.ahk(KB.Enter)
    controller.ahk(KB.Down, 2)
    controller.ahk(KB.Enter)
    controller.ahk(KB.Down, 4)
    controller.ahk(KB.Enter, 2)
    controller.ahk(GB.Menu, delay=0)


