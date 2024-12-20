from ..conf.bindings import GameBindings as GB
class Weapon:
    def __init__(self):
        self.current=GB.Weapons.Pistol
        self.last=GB.Weapons.Pistol
        self.weapon_list = GB.Weapons.Weapon_list
        self.pistol = GB.Weapons.Pistol
        self.machine_gun = GB.Weapons.Machine_gun
        self.rifle = 5
        self.sniper = 7
        self.melee_weapon = 1
        self.hand = 9
        self.shot_gun = 2
        self.heavy_weapon = 4
        self.special_weapon = 3
        pass
    def set_current_weapon(self,weapon):
        self.current=weapon
    def set_last_weapon(self,weapon):
        self.last=weapon