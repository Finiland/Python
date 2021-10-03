import random
import math
import json
import time
import numpy
import os

from discord.ext.commands.core import check
import LootTable



levels = [0,83,174,276,388,512,650,801,969,1154,1358,1584,1833,2107,2411,2746,3115,3523,3973,4470,5018,5624,6291,7028,7842,8740,9730,10824,12031,13363,14833,16456,18247,20224,22406,24815,27473,30408,33648,37224,41171,45529,50339,55649,61512,67983,75127,83014,91721,101333,111945,123660,136594,150872,166636,184040,203254,224466,247886,273742,302288,333804,368599,407015,449428,496254,547953,605032,668051,737627,814445,899257,992895,1096278,1210421,1336443,1475581,1629200,1798808,1986068,2192818,2421087,2673114,2951373,3258594,3597792,3972294,4385776,4842295,5346332,5902831,6517253,7195629,7944614,8771558,9684577,10692629,11805606,13034431,14391160,15889109,17542976,19368992,21385073,23611006,26068632,28782069,31777943,35085654,38737661,42769801,47221641,52136869,57563718,63555443,70170840,77474828,85539082,94442737,104273167,115126838,127110260,140341028,154948977,171077457,188884740]

pickaxes = {
    "Bronze pickaxe": {
        "name": "Bronze pickaxe",
        "reduction": 0.95,
        "level": 1,
        "reduction_number": 5,
    },
    "Iron pickaxe": {
        "name": "Iron pickaxe",
        "reduction": 0.90,
        "level": 1,
        "reduction_number": 10,
},
    "Steel pickaxe": {
        "name": "Steel pickaxe",
        "reduction": 0.85,
        "level": 5,
        "reduction_number": 15,
},
    "Black pickaxe": {
        "name": "Black pickaxe",
        "reduction": 0.80,
        "level": 11,
        "reduction_number": 20,
}, 
    "Mithril pickaxe": {
        "name": "Mithril pickaxe",
        "reduction": 0.75,
        "level": 21,
        "reduction_number": 25,
}, 
    "Adamant pickaxe": {
        "name": "Adamant pickaxe",
        "reduction": 0.70,
        "level": 31,
        "reduction_number": 30,
}, 
    "Rune pickaxe": {
        "name": "Rune pickaxe",
        "reduction": 0.65,
        "level": 41,
        "reduction_number": 35,
}, 
    "Dragon pickaxe": {
        "name": "Dragon pickaxe",
        "reduction": 0.55,
        "level": 61,
        "reduction_number": 45,
}, 
    "Infernal pickaxe": {
        "name": "Infernal pickaxe",
        "reduction": 0.5,
        "level": 71,
        "reduction_number": 50,
}, 
    "3rd age pickaxe": {
        "name": "3rd age pickaxe",
        "reduction": 0.30,
        "level": 71,
        "reduction_number": 70,
}, 
    "Crystal pickaxe": {
        "name": "Crystal pickaxe",
        "reduction": 0.45,
        "level": 71,
        "reduction_number": 55,
}, 
}

class Rocks(object):
    class Clay(object):
        name = "Clay"
        xp = 5
        level = 1
        loot = "Clay"
        loot_name = "Clay"
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class RuneEssence(object):
        name = "Rune essence"
        xp = 5
        level = 1
        loot = "Rune essence"
        loot_name = "Rune essence"
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Copper(object):
        name = "Copper"
        xp = 17.5
        level = 1
        loot = "Copper ore"
        loot_name = "Copper ore"
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Tin(object):
        name = "Tin"
        xp = 17.5
        level = 1
        loot = "Tin ore"
        loot_name = "Tin ore"
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Limestone(object):
        name = "Limestone"
        xp = 26.5
        level = 10
        loot = "Limestone"
        loot_name = "Limestone"
        time = 1.1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Blurite(object):
        name = "Blurite"
        xp = 17.5
        level = 10
        loot = "Blurite ore"
        loot_name = "Blurite ore"
        time = 1.1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Iron(object):
        name = "Iron"
        xp = 35
        level = 15
        loot = "Iron ore"
        loot_name = "Iron ore"
        time = 1.15
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Daeyalt(object):
        name = "Daeyalt"
        xp = 5
        level = 20
        loot = "Daeyalt ore"
        loot_name = "Daeyalt ore"
        time = 1.2
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Silver(object):
        name = "Silver"
        xp = 40
        level = 20
        loot = "Silver ore"
        loot_name = "Silver ore"
        time = 1.2
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class VolcanicAsh(object):
        name = "Volcanic ash"
        xp = 10
        level = 22
        loot = "Volcanic ash"
        loot_name = "Volcanic ash"
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PureEssence(object):
        name = "Pure essence"
        xp = 5
        level = 30
        loot = "Pure essence"
        loot_name = "Pure essence"
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Coal(object):
        name = "Coal"
        xp = 50
        level = 30
        loot = "Coal"
        loot_name = "Coal"
        time = 1.3
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class GemRock(object):
        name = "Gem"
        xp = 65
        level = 40
        gems = "Uncut opal", "Uncut jade", "Uncut red topaz", "Uncut sapphire", "Uncut emerald", "Uncut ruby", "Uncut diamond"
        random_gem = gems
        loot = random_gem
        loot_name = random_gem
        time = 1.3
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Gold(object):
        name = "Gold"
        xp = 65
        level = 40
        loot = "Gold ore"
        loot_name = "Gold ore"
        time = 1.3
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Mithril(object):
        name = "Mithril"
        xp = 80
        level = 55
        loot = "Mithril ore"
        loot_name = "Mithril ore"
        time = 2
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Adamantite(object):
        name = "Adamantite"
        xp = 95
        level = 70
        loot = "Adamantite ore"
        loot_name = "Adamantite ore"
        time = 3
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class SoftClay(object):
        name = "Soft clay"
        xp = 5
        level = 70
        loot = "Soft clay"
        loot_name = "Soft clay"
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Runite(object):
        name = "Runite"
        xp = 125
        level = 85
        loot = "Runite ore"
        loot_name = "Runite ore"
        time = 4
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class Amethyst(object):
        name = "Amethyst"
        xp = 240
        level = 92
        loot = "Amethyst"
        loot_name = "Amethyst"
        time = 5
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"

def mineChoiceRocks():
    with open("stats.json", 'r') as f:
            data = json.load(f)
            f.close()
    level = data['mining level']
    miningXp = data['mining xp']
    levelChecker()
    cutChoice = input("What kind of rock you would want to mine? Here are your possibilities: 1. Clay (1), 2. Rune essence (1), 3. Copper (1), 4. Tin (1), 5. Limestone (10) \n 6. Blurite (10), 7. Iron (15), 8. Daeyalt (20), 9. Silver (20), 10. Volcanic Ash (22), 11. Pure Essence (30), 12. Coal (30), 13. Gems (40)\n 14. Gold (40), 15. Mithril (55), 16. Adamantite (70), 17. Soft clay (70), 18. Runite (85), 19. Amethyst (92)\n")
    if cutChoice == "1":
        RockType = Rocks.Clay
        print("You have selected", RockType.name,"... Here some info about it")
        print("Name - ", RockType.name)
        print("XP - ", RockType.xp)
        print("Level - ", RockType.level)
        print("Loot - ", RockType.loot)
        print("Time per a mine - ", RockType.time, "seconds")
        cutState(RockType, miningXp)
        levelChecker()
        return RockType
    elif cutChoice == "2":
        RockType = Rocks.RuneEssence
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "3":
        RockType = Rocks.Copper
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "4":
        RockType = Rocks.Tin
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "5":
        RockType = Rocks.Limestone
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "6":
        RockType = Rocks.Blurite
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "7":
        RockType = Rocks.Iron
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "8":
        RockType = Rocks.Daeyalt
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "9":
        RockType = Rocks.Silver
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "10":
        RockType = Rocks.VolcanicAsh
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "11":
        RockType = Rocks.PureEssence
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "12":
        RockType = Rocks.Coal
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "13":
        RockType = Rocks.GemRock
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.gems)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "14":
        RockType = Rocks.Gold
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "15":
        RockType = Rocks.Mithril
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "16":
        RockType = Rocks.Adamantite
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "17":
        RockType = Rocks.SoftClay
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "18":
        RockType = Rocks.Runite
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "19":
        RockType = Rocks.Amethyst
        if RockType.level > level:
            print("Your Mining level is not high enough to mine ", RockType.name, ". You need to get level", RockType.level, "Your Mining level currently:", level)
            mineChoiceRocks()
        else:
            print("You have selected", RockType.name,"... Here some info about it")
            print("Name - ", RockType.name)
            print("XP - ", RockType.xp)
            print("Level - ", RockType.level)
            print("Loot - ", RockType.loot)
            print("Time per a mine - ", RockType.time, "seconds")
            cutState(RockType, miningXp)
            levelChecker()
            return RockType
    elif cutChoice == "hacks":
        LootTable.addItemToBank(Rocks.Clay.loot_name, 1)
        LootTable.addItemToBank(Rocks.RuneEssence.loot_name, 1)
        LootTable.addItemToBank(Rocks.Copper.loot_name, 1)
        LootTable.addItemToBank(Rocks.Tin.loot_name, 1)
        LootTable.addItemToBank(Rocks.Limestone.loot_name, 1)
        LootTable.addItemToBank(Rocks.Blurite.loot_name, 1)
        LootTable.addItemToBank(Rocks.Iron.loot_name, 1)
        LootTable.addItemToBank(Rocks.Daeyalt.loot_name, 1)
        LootTable.addItemToBank(Rocks.Silver.loot_name, 1)
        LootTable.addItemToBank(Rocks.VolcanicAsh.loot_name, 1)
        LootTable.addItemToBank(Rocks.PureEssence.loot_name, 1)
        LootTable.addItemToBank(Rocks.Coal.loot_name, 1)
        LootTable.addItemToBank(Rocks.GemRock.loot_name, 1)
        LootTable.addItemToBank(Rocks.Gold.loot_name, 1)
        LootTable.addItemToBank(Rocks.Gold.loot_name, 1)
        LootTable.addItemToBank(Rocks.Mithril.loot_name, 1)
        LootTable.addItemToBank(Rocks.Adamantite.loot_name, 1)
        LootTable.addItemToBank(Rocks.SoftClay.loot_name, 1)
        LootTable.addItemToBank(Rocks.Runite.loot_name, 1)
        LootTable.addItemToBank(Rocks.Amethyst.loot_name, 1)
        mineChoiceRocks()        
    else:
        time.sleep(1)
        os.system('clear')
        mineChoiceRocks()
def cutState(RockType, miningXp):
    with open("bank.json", "r") as f:
        data = json.load(f)
        f.close()
    with open("stats.json", 'r') as f:
        level2 = json.load(f)
        f.close()
    if pickaxes["Crystal pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Crystal pickaxe"]["level"]:
        current_axe = pickaxes["Crystal pickaxe"]
    else:
        if pickaxes["3rd age pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["3rd age pickaxe"]["level"]:
            current_axe = pickaxes["3rd age pickaxe"]
        else:
            if pickaxes["Infernal pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Infernal pickaxe"]["level"]:
                current_axe = pickaxes["Infernal pickaxe"]
            else:
                if pickaxes["Dragon pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Dragon pickaxe"]["level"]:
                    current_axe = pickaxes["Dragon pickaxe"]
                else:
                    if pickaxes["Rune pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Rune pickaxe"]["level"]:
                        current_axe = pickaxes["Rune pickaxe"]
                    else:
                        if pickaxes["Adamant pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Adamant pickaxe"]["level"]:
                            current_axe = pickaxes["Adamant pickaxe"]
                        else:
                            if pickaxes["Mithril pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Mithril pickaxe"]["level"]:
                                current_axe = pickaxes["Mithril pickaxe"]
                            else:
                                if pickaxes["Black pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Black pickaxe"]["level"]:
                                    current_axe = pickaxes["Black pickaxe"]
                                else:
                                    if pickaxes["Steel pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Steel pickaxe"]["level"]:
                                        current_axe = pickaxes["Steel pickaxe"]
                                    else:
                                        if pickaxes["Iron pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Iron pickaxe"]["level"]:
                                            current_axe = pickaxes["Iron pickaxe"]
                                        else:
                                            if pickaxes["Bronze pickaxe"]["name"] in data and level2['mining level'] >= pickaxes["Bronze pickaxe"]["level"]:
                                                current_axe = pickaxes["Bronze pickaxe"]
                                            else:
                                                current_axe = None
    if current_axe != None:        
        if RockType == Rocks.GemRock:
            random_gem_random = random.choice(Rocks.GemRock.random_gem)
            time.sleep(RockType.time * current_axe["reduction"])
            os.system('clear')
            print("############## YOU ARE MINING", current_axe["reduction_number"], "%", "FASTER BECAUSE OF YOUR", current_axe["name"], "##############")
            print("You managed to get 1", random_gem_random)
            print("You gained", RockType.xp, "XP")
            with open("stats.json", "r") as f:
                data = json.load(f)
                f.close()
            miningXp = data['mining xp']
            miningXp = int(miningXp) + RockType.xp
            miningLevel = int(data['mining level'])
            print("You have now", float(miningXp), "in Mining skill. Level is:", int(miningLevel))
            if (f"{levels[int(miningLevel)] - int(miningXp)}") > str(0):    
                print(f"{levels[int(miningLevel)] - int(miningXp)} xp remaining for next level:", miningLevel + 1)
            else:
                print("0 xp remaining for next level:", miningLevel + 1)
            print(f"You have to mine: {math.ceil((levels[int(miningLevel)] - int(miningXp)) / RockType.xp)} rocks.")
            LootTable.addItemToBank(random_gem_random, RockType.amount)
            LootTable.checkItemFromBank(random_gem_random, RockType.amount)
            print(f"Banked the materials into your bank. Currently you have:{LootTable.checkItemFromBank(random_gem_random, RockType.amount)}")
        else:
            time.sleep(RockType.time * current_axe["reduction"])
            os.system('clear')   
            print("############## YOU ARE MINING", current_axe["reduction_number"], "%", "FASTER BECAUSE OF YOUR", current_axe["name"], "##############")
            print("You managed to get 1", RockType.loot_name)
            print("You gained", RockType.xp, "XP")
            with open("stats.json", "r") as f:
                data = json.load(f)
                f.close()
            miningXp = data['mining xp']
            miningXp = int(miningXp) + RockType.xp
            miningLevel = data['mining level']
            print("You have now", float(miningXp), "in Mining skill. Level is:", int(miningLevel))
            if (f"{levels[int(miningLevel)] - int(miningXp)}") > str(0):    
                print(f"{levels[int(miningLevel)] - int(miningXp)} xp remaining for next level:", miningLevel + 1)
            else:
                print("0 xp remaining for next level:", miningLevel + 1)
            print(f"You have to mine: {math.ceil((levels[int(miningLevel)] - int(miningXp)) / RockType.xp)} rocks.")
            LootTable.addItemToBank(RockType.loot_name, RockType.amount)
            LootTable.checkItemFromBank(RockType.loot_name, RockType.amount)

        print(f"Banked the logs into your bank. Currently you have:{LootTable.checkItemFromBank(RockType.loot_name, RockType.amount)}")
        xpChecker(RockType)
        levelChecker()
        cutState(RockType, miningXp)
        return miningXp, Rocks.GemRock.random_gem
    if current_axe == None:
        if RockType == Rocks.GemRock:
            random_gem_random = random.choice(Rocks.GemRock.random_gem)
            time.sleep(RockType.time)
            os.system('clear') 
            print("You managed to get 1", random_gem_random)
            print("You gained", RockType.xp, "XP")
            with open("stats.json", "r") as f:
                data = json.load(f)
                f.close()
            miningXp = data['mining xp']
            miningXp = int(miningXp) + RockType.xp
            miningLevel = int(data['mining level'])
            print("You have now", float(miningXp), "in Mining skill. Level is:", int(miningLevel))
            if (f"{levels[int(miningLevel)] - int(miningXp)}") > str(0):    
                print(f"{levels[int(miningLevel)] - int(miningXp)} xp remaining for next level:", miningLevel + 1)
            else:
                print("0 xp remaining for next level:", miningLevel + 1)
            print(f"You have to mine: {math.ceil((levels[int(miningLevel)] - int(miningXp)) / RockType.xp)} rocks.")
            LootTable.addItemToBank(random_gem_random, RockType.amount)
            LootTable.checkItemFromBank(random_gem_random, RockType.amount)
            print(f"Banked the materials into your bank. Currently you have:{LootTable.checkItemFromBank(random_gem_random, RockType.amount)}")
        else:
            time.sleep(RockType.time)
            os.system('clear') 
            print("You managed to get 1", RockType.loot_name)
            print("You gained", RockType.xp, "XP")
            with open("stats.json", "r") as f:
                data = json.load(f)
                f.close()
            miningXp = data['mining xp']
            miningXp = int(miningXp) + RockType.xp
            miningLevel = int(data['mining level'])
            print("You have now", float(miningXp), "in Mining skill. Level is:", int(miningLevel))
            if (f"{levels[int(miningLevel)] - int(miningXp)}") > str(0):    
                print(f"{levels[int(miningLevel)] - int(miningXp)} xp remaining for next level:", miningLevel + 1)
            else:
                print("0 xp remaining for next level:", miningLevel + 1)
            print(f"You have to mine: {math.ceil((levels[int(miningLevel)] - int(miningXp)) / RockType.xp)} rocks.")
            LootTable.addItemToBank(RockType.loot_name, RockType.amount)
            LootTable.checkItemFromBank(RockType.loot_name, RockType.amount)
            print(f"Banked the materials into your bank. Currently you have:{LootTable.checkItemFromBank(RockType.loot_name, RockType.amount)}")
        xpChecker(RockType)
        levelChecker()
        cutState(RockType, miningXp)
        return miningXp, Rocks.GemRock.random_gem

def xpChecker(RockType):
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    data['mining xp'] = int(data['mining xp']) + RockType.xp
    data['total xp'] = int(data['total xp']) + RockType.xp
    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()




def levelChecker():
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    miningXp = data['mining xp']
    miningLevel = data['mining level']
    if int(miningXp) >= levels[int(miningLevel)]:
            data['mining level'] = int(data['mining level']) + 1
            data['total level'] = int(data['total level']) + 1
            print(f"You got a new level! Current level is: {int(miningLevel) + 1} ")
    with open("stats.json", 'w') as f:
        data = json.dump(data, f, indent=4)
        f.close()