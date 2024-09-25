from os.path import join, dirname
from KeyBindings import GameKeyBindings

class Process:
    Game_Name = "Grand Theft Auto V"

    class ProcessNames:
        Process_GTA = "GTA5.exe"
        Process_BE="GTA5_BE.exe"
        Process_Launcher = "Launcher.exe"
        Process_Play_GTA5 = "PlayGTAV.exe"
        Process_Rockstar_Service = "RockstarService.exe"
        Process_Error_Handler = "RockstarErrorHandler.exe"
        Process_SC_Helper = "SocialClubHelper.exe"

    class ProcessPids:
        Process_GTA = None
        Process_BE=None
        Process_Launcher = None
        Process_Play_GTA5 = None
        Process_Rockstar_Service = None
        Process_Error_Handler = None
        Process_SC_Helper = None


class Listener:
    Mouse = None
    Keyboard = None
    Mouse_Controller=None
    Keyboard_Controller=None


class KeyStatus:
    X2_Pressed = False
    Left_Pressed = False
    Space_Pressed = False
    Tab_Pressed = False


class GameParmas:
    Weapon_Mapping = {
        0: GameKeyBindings.Weapons.Pistol,
        1: GameKeyBindings.Weapons.Machine_gun,
        2: GameKeyBindings.Weapons.Rifle,
        3: GameKeyBindings.Weapons.Sniper,
        4: GameKeyBindings.Weapons.Melee_weapon,
        5: GameKeyBindings.Weapons.Shot_gun,
        6: GameKeyBindings.Weapons.Heavy_weapon,
        7: GameKeyBindings.Weapons.Special_weapon
    }
    Is_Suspend=False


class AppParmas:
    Icon_Path = join(dirname(__file__), "icon.png")
    Icon = None

class Inital:
    pass
