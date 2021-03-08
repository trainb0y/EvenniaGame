

from world.spells import *


class BaseClass:
    def __init__(self):
        self.name = "Peasant"
        self.desc = "Commoner, peasant, whatever you want to call it."
        self.bonus_hp = 0
        self.bonus_armor = 0

        self.bonus_int = 0
        self.bonus_str = 0
        self.bonus_dex = 0
        self.bonus_magic = 0

        self.bonus_proficiencies = []
        self.bonus_spells = []
        self.bonus_tags = []

        self.bonus_resistances = []
        self.bonus_immunities = []
    
    def level_up(self, target, level):
        """Called when the character levels up"""

class Fighter(BaseClass):
    def __init__(self):
        super().__init__()
        self.name = "Fighter"
        self.desc = "One who specializes in the use of weapons on the battlefield"
        self.bonus_str = 1
        self.bonus_proficiencies += ["DAGGER","SWORD","AXE","BOW","MACE","UNARMED"]
    
    def level_up(self, target, level):
        if level == 5: target.strength += 1
        elif level == 10: target.strength += 2


class Mage(BaseClass):
    def __init__(self):
        super().__init__()
        self.name = "Mage"
        self.desc = "A person devoted to the discovery and usage of arcane secrets"
        self.bonus_int = 1
        self.bonus_magic = 1
        self.bonus_spells = [MagicMissile]

classes = [Fighter,Mage]