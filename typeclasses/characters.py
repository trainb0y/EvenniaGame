"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter




level_thresholds = [0]
increase = 10
for i in range(100):
    increase = round(increase * 1.1)
    old = level_thresholds[-1]
    level_thresholds.append(increase+old)
    
    


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    def setup(self): # Called by character creation menu
      
        self.db.level = 0
        self.db.xp = 0
        self.db.gold = 20

        race = self.db.race
        pclass = self.db.pclass

        self.db.max_hp = race.base_hp + pclass.bonus_hp
        self.db.tags = race.base_tags + pclass.bonus_tags

        self.db.strength = race.base_str_mod + pclass.bonus_str
        self.db.dexterity = race.base_dex_mod + pclass.bonus_dex
        self.db.intelligence = race.base_int_mod + pclass.bonus_int

        self.db.max_magic = race.base_max_magic_mod + pclass.bonus_magic

        self.db.spells = race.base_spells + pclass.bonus_spells
        self.db.proficiencies = race.base_proficiencies + pclass.bonus_proficiencies

        self.db.armor = race.base_armor + pclass.bonus_armor

        self.db.magic = self.db.max_magic # Magic starts full, of course
        self.db.hp = self.db.max_hp # Same with health

        self.db.resistances = race.base_resistances + pclass.bonus_resistances
        self.db.immunities = race.base_immunities + pclass.bonus_immunities

    
    def get_armor(self):
        return self.db.armor # eventually will want to scan inventory for bonuses to armor and such
    


    
    def gain_xp(self, amount):
        """Add xp and check for level up"""
        self.db.xp += amount
        for level in level_thresholds:
            if self.db.xp < level: # If the xp is less, that means that the previous level
                           # is the one the player is at
                new_level = level_thresholds.index(level) - 1
                break
        if new_level > self.db.level:
            # Level up!
            self.db.level = new_level
            self.db.race.level_up(self,self.db.level)
            self.db.pclass.level_up(self, self.db.level)
