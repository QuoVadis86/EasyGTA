from conf.bindings import GameBindings as GB

class Weapon():
    def __init__(self):
        self.current=self.f(GB.Weapons.Pistol)
        self.last=self.f(GB.Weapons.Pistol)
        self.weapon_list = self.f(GB.Weapons.Weapon_list)
        self.pistol = self.f(GB.Weapons.Pistol)
        self.machine_gun = self.f(GB.Weapons.Machine_gun)
        self.rifle = self.f(GB.Weapons.Rifle)
        self.sniper = self.f(GB.Weapons.Sniper)
        self.melee_weapon = self.f(GB.Weapons.Melee_weapon)
        self.hand = self.f(GB.Weapons.Hand)
        self.shot_gun = self.f(GB.Weapons.Shot_gun)
        self.heavy_weapon = self.f(GB.Weapons.Heavy_weapon)
        self.special_weapon = self.f(GB.Weapons.Special_weapon)

    def f(self,key):
        return key