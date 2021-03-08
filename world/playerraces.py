
class BaseRace:
    def __init__(self):
        self.base_str_mod = 0
        self.base_dex_mod = 0
        self.base_int_mod = 0
        self.base_max_magic_mod = 0
        self.base_armor = 0
        self.base_hp = 10
        self.size = 2 # Medium
        self.name = "BaseRace"
        self.desc = "A shapeless humanoid"
        self.base_spells = []
        self.base_proficiencies = []
        self.base_tags = [] # The list of tags like NIGHTVISION or FLIES
        self.prestige_required = 0

        self.base_resistances = []
        self.base_immunities = []
        

    def level_up(self, target, level):
        """Called when the character levels up"""



class Human(BaseRace):
    def __init__(self):
        super().__init__()
        self.name = "Human"
        self.desc = "An example of ordinary mankind, and a Jack-of-all trades"

class Elf(BaseRace):
    def __init__(self):
        super().__init__()
        self.name = "Elf"
        self.desc = "Tall and lean, elves range the wilds in search of natural peace and beauty"
        self.base_dex_mod = 2
        self.base_int_mod = 1
        self.base_max_magic_mod = 2
        self.prestige_required = 1

        # Need to add some spells
        
class Dwarf(BaseRace):
    def __init__(self):
        super().__init__()
        self.name = "Dwarf"
        self.desc = "Short, sturdy creatures fond of drink and industry."
        self.base_proficiencies.append("AXE")
        self.base_armor = 1
        self.base_str_mod = 2
        self.size = 1 # Small
        self.prestige_required = 1

class Orc(BaseRace):
    def __init__(self):
        super().__init__()
        self.name = "Orc"
        self.desc = "Large, but rather dumb, Orcs generally value braun over brains."
        self.base_armor = 1
        self.base_str_mod = 4
        self.base_int_mod = -2
        self.size = 3 # Large
        self.base_hp = 15
        self.prestige_required = 2

class Wolfkin(BaseRace):
    def __init__(self):
        super().__init__()
        self.name = "Wolfkin"
        self.desc = "Humanoid wolves covered in fur and muscle, wolfkin prowl the wilds in search of evil."
        self.base_armor = 1
        self.base_str_mod = 3
        self.base_dex_mod = 1
        self.base_hp = 12
        self.prestige_required = 3

        # Some sort of claw/bite attack

class DarkElf(BaseRace):
    def __init__(self):
        super().__init__()
        self.name = "Dark Elf"
        self.desc = "Elves tainted with evil power, most dark elves are strong enemies of the light."
        self.base_dex_mod = 3
        self.base_magic_mod = 5
        self.base_int_mod = 2
        self.base_tags.append("NIGHTVISION")
        self.prestige_required = 3
        
        # Need to add spells

class Lizardfolk(BaseRace):
    def __init__(self):
        super().__init__()
        self.name = "Lizardfolk"
        self.desc = "Scaly, amphibious, lizard-like humanoids, lizardfolk make thier homes in the vicious swamps of the west."
        self.base_str_mod = 2
        self.base_armor = 5
        self.base_tags.append("AMPHIBIOUS")
        self.base_tags.append("NIGHTVISION")
        self.prestige_required = 3
        self.base_resistances.append("POISON")

class Dragon(BaseRace): # Lol idk why I added any of this.
    def __init__(self):
        super().__init__()
        self.name = "Dragon"
        self.desc = "Magestic, flying, fire-breathing lizards of awesome power."
        self.base_str_mod = 3
        self.size = 3 # Large
        self.base_armor = 5
        self.base_hp = 200
        self.base_dex_mod = 3
        self.base_magic_mod = 5
        self.base_int_mod = 2
        self.base_tags.append("NIGHTVISION")
        self.base_tags.append("FLIES")
        self.base_immunities.append("FIRE")
        self.prestige_required = 100

races = [Human, Elf, Dwarf, Orc, Wolfkin, DarkElf, Lizardfolk]