from os.path import join, dirname
from conf.bindings import GameKeyBindings

class Names:
    GAME_NAME = "Grand Theft Auto V"
    GTA5 = "GTA5.exe"
    BE="GTA5_BE.exe"
    LAUNCHER = "Launcher.exe"
    PLAY_GTA5 = "PlayGTAV.exe"
    ROCKSTAR_SERVICE = "RockstarService.exe"
    ERROR_HANDLER = "RockstarErrorHandler.exe"
    SC_HELPER = "SocialClubHelper.exe"
    



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


# class AppParmas:
#     Icon_Path = join(dirname(__file__), "icon.png")
#     Icon = None

# class Inital:
#     pass
