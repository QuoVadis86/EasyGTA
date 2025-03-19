#按键绑定配置文件
from pynput.keyboard import Key
from pynput.mouse import Button
class Game:
    Menu = "m"


class App:
  
    Start_Engine = Key.f5
    Suspend = Key.end
    Kill = Key.delete
    Reload_App = Key.f6
    Net_Limit=Key.f7


class KeyBoard:
    Esc = Key.esc
    Space = Key.space
    Up = Key.up
    Down = Key.down
    Left = Key.left
    Right = Key.right
    Enter = Key.enter
    Back = Key.backspace
    Del=Key.delete

class Mouse:
   
    X1 =Button.x1
    X2 = Button.x2