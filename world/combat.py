#!python3
import random, time
from evennia import default_cmds
from world.misc import roll
class CmdCast(default_cmds.MuxCommand):
    """ 
    Cast a spell

    Usage:
      cast <target> <spell name/id>

    Note: If the spell name is multiple words,
    enclose it in "s as in "Magic Missile"
    """
    key = "cast"
    aliases = ["ca"]

    def func(self):
        # get the target
        target = self.caller.search(self.target)              
        if not target:
            return 

        
        

class CmdAttack(default_cmds.MuxCommand):
    """ 
    Attack a target

    Usage:
      attack <player> [with <weapon>]

    """
    key = "attack"
    aliases = ["kill","k"]

    def parse(self):
        self.args = self.args.strip()
        target, *weapon = self.args.split(" with ", 1)
        if not weapon:
            target, *weapon = target.split(" ", 1)          
        self.target = target.strip() 
        if weapon:
            self.weapon = weapon.strip()
        else:
            self.weapon = ""

    def func(self):

        "Implement the spell"
    

        now = time.time()   
        if hasattr(self, "last_attack") and \
                now - self.last_attack < 3: # 3 second cooldown
            self.caller.msg("You can't attack again yet!")
            return 
        

        # get the target
        target = self.caller.search(self.target)              
        if not target:
            return 
        
        weapon = False
        if self.weapon:
            weapon = self.caller.search(self.weapon)
        if weapon: 
            weapon_name = f"{weapon.key}"
            hit_bonus = 0 # Add the applicable stat/bonuses
            dam_bonus = 0 # from stats and such
            damage_dice = weapon.db.damage if weapon.db.damage is not None else None
            damage_type = weapon.db.damage_type if weapon.db.damage_type is not None else None
        else:
            hit_bonus = 0 # Add the applicable stat/bonuses
            dam_bonus = 0 # from stats and such
            weapon_name = "fists"
            damage_dice = "1d4"
            damage_type = "MELEE"

        

        # Determine if this hits:
        hit = random.choice([True,False]) 
        # ^^ will probably want a more advanced system someday
        # using hit_bonus that is
        if hit:
            damage = roll(damage_dice) + dam_bonus
            damage_string = f"{damage} {damage_type.lower()}"

            if damage_type not in target.db.immunities: # if its not immune, is it resistant?
                if damage_type in target.db.resistances: damage = damage // 2

                if damage_type == "MELEE": # if it isn't melee, armor is half as effective.
                    damage -= target.get_armor()
                else: damage -= target.get_armor() // 2 


                if damage < 0: damage = 0 # did the armor or modifiers make it negative? fix that
                target.db.hp -= damage

            if damage == 0: # it clanged off of their armor kind of thing
                if target.db.armor > 0 and random.choice([True,True,False]): # 33% chance to do the other no damage message
                    self.caller.msg(f"You hit {target.key} with your {weapon_name}, but it bounces away harmlessly.")
                    target.msg(f"{self.caller.key} hits you with their {weapon_name}, but it bounces away harmlessly.")
                else: # just rolled bad or 1/3 chance if armor deflected
                    self.caller.msg(f"You hit {target.key} with your {weapon_name}, but your pitiful attack deals no damage.")
                    target.msg(f"{self.caller.key}'s pitiful attack with their' {weapon_name} deals no damage")

            else: # there was damage
                self.caller.msg(f"You hit {target.key} with your {weapon_name}, dealing {damage_string} damage!") 
                target.msg(f"{self.caller.key} hit you with their {weapon_name} for {damage_string} damage!")

        else: # miss
            self.caller.msg(f"You miss {target.key}") 
            target.msg(f"{self.caller.key} misses you with their {weapon_name}!")
        
        self.last_attack = now 
