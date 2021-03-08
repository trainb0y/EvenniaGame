class BaseSpell:
    def __init__(self):
        self.name = "Base Spell"
        self.id = 0 # so "cast 0 orc" works
        self.magic_cost = 0
        self.healing = False # If healing, heals damage instead of deals
        self.damage_type = "MAGIC"
        # Valid damage types:
        # MELEE, POISON, ACID, COLD, FIRE, MAGIC
        self.damage = "1d1"


class MagicMissile(BaseSpell):
    def __init__(self):
        super().__init__()
        self.name = "Magic Missile"
        self.id = 1
        self.magic_cost = 1
        self.damage = "1d6+1"

class Fireball(BaseSpell):
    def __init__(self):
        super().__init__()
        self.name = "Fireball"
        self.id = 2
        self.damage_type = "FIRE"
        self.damage = "2d8"

class SmallHeal(BaseSpell):
    def __init__(self):
        super().__init__()
        self.name = "Small Heal"
        self.id = 3
        self.healing = True
        self.damage = "1d12"

spells = [MagicMissile(),Fireball(),SmallHeal()]