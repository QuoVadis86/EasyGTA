from threading import Thread
import run
from conf.binding import Game as GB
from conf.binding import KeyBoard as KB
from conf.binding import App as AB
from conf.config import *


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

def exit_app():
   

def restart():
    
