from entity.input import Input
from entity.weapon import Weapon
from entity.process import GTA
from entity.listener import Listener

input: Input
process: GTA
weapon: Weapon
listener: Listener
# is_suspend=False

x2_pressed = False
left_pressed = False
space_pressed = False
tab_pressed = False

def init():
    global input, process, weapon, listener
    input = Input()
    process = GTA()
    weapon = Weapon()
    listener = Listener()
