from evennia.utils import evmenu, evtable
from world import playerraces, playerclasses



def menunode_racelist(caller):
    "This is the top-menu screen for race selection."

    # Have to check if this has already been run. If so, abort.
    if caller.db.race != None:
        caller.msg("|yYou have already set up your character!|n\n")
        return None, None

    text = "*** Choose a Race ***\n"
    
    text += "   Races (choose 1-%i to inspect);" \
            " quit to exit:" % len(playerraces.races)
 
    options = []
    for race in playerraces.races:
        # add an option for every ware in store
        options.append({"desc": "%s: %s" %
                             (race().name, race().desc),
                        "goto": "menunode_inspect_and_select_race"})
    return text, options



def menunode_inspect_and_select_race(caller, raw_string):
    "Sets up the race selection menu screen."

    irace = int(raw_string) - 1
    race = playerraces.races[irace]
    text = "You inspect %s:\n\n%s" % (race().name, race().desc) 

    # gather statistics and create table
 
    r = race()
    stat_table = evtable.EvTable("Stat","Bonus",table=[
        ["int","str","dex","mag","hp","armor","size","PR req"],
        [r.base_int_mod,r.base_str_mod,r.base_dex_mod,r.base_max_magic_mod,r.base_hp,r.base_armor,r.size,r.prestige_required]])
    text += "\n" + "\n".join(stat_table.get()) + "\n\n"
    if len(r.base_proficiencies) != 0: text += "Proficiencies: "+str(r.base_proficiencies)+"\n"
    if len(r.base_spells) != 0: text += "Spells: "+str(r.base_spells)+"\n"
    if len(r.base_tags) != 0: text += "Tags: "+str(r.base_tags)+"\n"
    if len(r.base_resistances) != 0: text += "Resistances: "+str(r.base_resistances)+"\n"
    if len(r.base_immunities) != 0: text += "Proficiencies: "+str(r.base_immunities)+"\n"


    def select_race_result(caller):
        "This will be executed first when selected"
        if caller.account.db.prestige >= race().prestige_required:
            caller.msg("You selected %s" % (race().name))
            caller.db.race = race()
            return "menunode_classlist"
        else:
            caller.msg("|yYou do not have high enough prestige to choose this race.|n")
            caller.msg(f"|y(Have {caller.account.db.prestige} need {race().prestige_required})")
            return "menunode_racelist"
    


    options = ({"desc": "Select race %s" % \
                        (race().name),
                "goto": select_race_result},
            
               {"desc": "Choose a different race",
                "goto": "menunode_racelist"})

    return text, options


def menunode_classlist(caller):
    "This is the top-menu screen for race selection."

    # Wares includes all items inside the storeroom, including the
    # door! Let's remove that from our for sale list.

    text = "*** Choose a Class ***\n"
    
    text += "   Classes (choose 1-%i to inspect);" \
            " quit to exit:" % len(playerclasses.classes)
 
    options = []
    for pclass in playerclasses.classes:
        # add an option for every ware in store
        options.append({"desc": "%s: %s" %
                             (pclass().name, pclass().desc),
                        "goto": "menunode_inspect_and_select_class"})
    return text, options



def menunode_inspect_and_select_class(caller, raw_string):
    "Sets up the race selection menu screen."

    # Don't forget, we will need to remove that pesky door again!
    iclass = int(raw_string) - 1
    pclass = playerclasses.classes[iclass]
    text = "You inspect %s:\n\n%s" % (pclass().name, pclass().desc)

    c = pclass()
    stat_table = evtable.EvTable("Stat","Bonus",table=[
    ["int","str","dex","magic","hp","armor"],
    [c.bonus_int,c.bonus_str,c.bonus_dex,c.bonus_magic,c.bonus_hp,c.bonus_armor]])
    text += "\n" + "\n".join(stat_table.get()) + "\n\n"
    if len(c.bonus_proficiencies) != 0: text += "Proficiencies: "+str(c.bonus_proficiencies)+"\n"
    if len(c.bonus_spells) != 0: text += "Spells: "+str([spell().name for spell in c.bonus_spells])+"\n"
    if len(c.bonus_tags) != 0: text += "Tags: "+str(c.bonus_tags)+"\n"
    if len(c.bonus_resistances) != 0: text += "Resistances: "+str(c.bonus_resistances)+"\n"
    if len(c.bonus_immunities) != 0: text += "Proficiencies: "+str(c.bonus_immunities)+"\n"

    def select_class_result(caller):
        "This will be executed first when selected"
       
        caller.msg("You selected %s" % (pclass().name))
        caller.db.pclass = pclass()

    options = ({"desc": "Select class %s" % \
                        (pclass().name),
                "goto": "menunode_select_gender",
                "exec": select_class_result},
               {"desc": "Choose a different class",
                "goto": "menunode_classlist"})

    return text, options


def menunode_select_gender(caller, raw_string):
    text = "*** Choose a gender ***"

    def select_gender_male(caller): caller.db.gender = "Male"
    def select_gender_female(caller): caller.db.gender = "Female"
    def select_gender_other(caller): caller.db.gender = "Other"

    options = ({"desc": "Male",
                "goto": "menunode_exit",
                "exec": select_gender_male},
               {"desc": "Female",
                "goto": "menunode_exit",
                "exec": select_gender_female},
                {"desc": "Other",
                "goto": "menunode_exit",
                "exec": select_gender_other}
                )
    return text, options


def menunode_exit(caller, raw_string):
    # Finish character setup
    caller.setup()
    #  Needs to teleport user out of Limbo, and into the world
    caller.move_to(4)
    
    return None, None # No options, ends menu

from evennia import Command

class CmdCharacterSetup(Command):
    """ 
    Select defining features for a character, such
    as race, class, and gender.

    Usage:
      charactersetup

    """
    key = "charactersetup"

    def func(self):
        "Starts the shop EvMenu instance"
        evmenu.EvMenu(self.caller,
                      "typeclasses.charactercreation",
                      startnode="menunode_racelist")

