import random
import math
import json
import time
import os

from discord.ext.commands.core import check
import LootTable



levels = [0,83,174,276,388,512,650,801,969,1154,1358,1584,1833,2107,2411,2746,3115,3523,3973,4470,5018,5624,6291,7028,7842,8740,9730,10824,12031,13363,14833,16456,18247,20224,22406,24815,27473,30408,33648,37224,41171,45529,50339,55649,61512,67983,75127,83014,91721,101333,111945,123660,136594,150872,166636,184040,203254,224466,247886,273742,302288,333804,368599,407015,449428,496254,547953,605032,668051,737627,814445,899257,992895,1096278,1210421,1336443,1475581,1629200,1798808,1986068,2192818,2421087,2673114,2951373,3258594,3597792,3972294,4385776,4842295,5346332,5902831,6517253,7195629,7944614,8771558,9684577,10692629,11805606,13034431,14391160,15889109,17542976,19368992,21385073,23611006,26068632,28782069,31777943,35085654,38737661,42769801,47221641,52136869,57563718,63555443,70170840,77474828,85539082,94442737,104273167,115126838,127110260,140341028,154948977,171077457,188884740]

axes = {
    "Bronze axe": {
        "name": "Bronze axe",
        "reduction": 0.95,
        "level": 1,
        "reduction_number": 5,
    },
    "Iron axe": {
        "name": "Iron axe",
        "reduction": 0.90,
        "level": 1,
        "reduction_number": 10,
},
    "Steel axe": {
        "name": "Steel axe",
        "reduction": 0.85,
        "level": 5,
        "reduction_number": 15,
},
    "Black axe": {
        "name": "Black axe",
        "reduction": 0.80,
        "level": 11,
        "reduction_number": 20,
}, 
    "Mithril axe": {
        "name": "Mithril axe",
        "reduction": 0.75,
        "level": 21,
        "reduction_number": 25,
}, 
    "Adamant axe": {
        "name": "Adamant axe",
        "reduction": 0.70,
        "level": 31,
        "reduction_number": 30,
}, 
    "Rune axe": {
        "name": "Rune axe",
        "reduction": 0.65,
        "level": 41,
        "reduction_number": 35,
}, 
    "Dragon axe": {
        "name": "Dragon axe",
        "reduction": 0.55,
        "level": 61,
        "reduction_number": 45,
}, 
    "Infernal axe": {
        "name": "Infernal axe",
        "reduction": 0.5,
        "level": 61,
        "reduction_number": 50,
}, 
    "3rd age axe": {
        "name": "3rd age axe",
        "reduction": 0.30,
        "level": 61,
        "reduction_number": 70,
}, 
    "Crystal axe": {
        "name": "Crystal axe",
        "reduction": 0.45,
        "level": 71,
        "reduction_number": 55,
}, 
}
class Trees(object):
    class NormalTree(object):
        name = "Logs"
        xp = 25
        level = 1
        loot = "Logs"
        loot_name = "Logs"
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class OakTree(object):
        name = "Oak"
        xp = 37.5
        level = 15
        loot = "Oak_Logs"
        loot_name = "Oak logs"
        time = 1.2
        amount = 1
    class WillowTree(object):
        name = "Willow"
        xp = 67.5
        level = 30
        loot = "Willow_Logs"
        loot_name = "Willow logs"
        time = 1.4
        amount = 1
    class TeakTree(object):
        name = "Teak"
        xp = 85
        level = 35
        loot = "Teak_Logs"
        loot_name = "Teak logs"
        time = 1.6
        amount = 1
    class MapleTree(object):
        name = "Maple"
        xp = 100
        level = 45
        loot = "Maple_Logs"
        loot_name = "Maple logs"
        time = 1.8
        amount = 1
    class BarkTree(object):
        name = "Bark"
        xp = 82.5
        level = 45
        loot = "Bark"
        loot_name = "Bark"
        time = 2
        amount = 1
    class MahoganyTree(object):
        name = "Mahogany"
        xp = 125
        level = 50
        loot = "Mahogany_Logs"
        loot_name = "Mahogany logs"
        time = 2.2
        amount = 1
    class ArcticTree(object):
        name = "Arctic pine"
        xp = 40
        level = 54
        loot = "Arctic_Pine_Logs"
        loot_name = "Arctic pine logs"
        time = 2.4
        amount = 1
    class YewTree(object):
        name = "Yew"
        xp = 175
        level = 60
        loot = "Yew_Logs"
        loot_name = "Yew logs"
        time = 2.6
        amount = 1
    class BlisterwoodTree(object):
        name = "Blisterwood"
        xp = 76
        level = 62
        loot = "Blisterwood_logs"
        loot_name = "Blisterwood logs"
        time = 2.7
        amount = 1
    class SulliuscepsTree(object):
        name = "Sulliusceps"
        xp = 127
        level = 65
        loot = "Sulliusceps"
        loot_name = "Sulliusceps"
        time = 2.8
        amount = 1
    class MagicTree(object):
        name = "Magic"
        xp = 250
        level = 75
        loot = "Magic_Logs"
        loot_name = "Magic logs"
        time = 3
        amount = 1
    class RedwoodTree(object):
        name = "Redwood"
        xp = 380
        level = 90
        loot = "Redwood_Logs"
        loot_name = "Redwood logs"
        time = 3.2
        amount = 1
    class ElderTree(object):
        name = "Elder"
        xp = 500
        level = 105
        loot = "Elder_Logs"
        loot_name = "Elder logs"
        time = 3.4
        amount = 1
    class HacksTree(object):
        name = "Hacks"
        xp = 1
        level = 1
        loot = "Logs"
        loot_name = "Logs", "Oak logs", "Willow logs", "Teak logs", "Maple logs", "Bark", "Mahogany logs", "Arctic pine logs", "Yew logs", "Blisterwood logs", "Sulliusceps", "Magic logs", "Redwood logs", "Elder logs"
        time = 0.01
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"

        
def stopping_maybe():
    with open("/home/linux/Documents/Python/Adventure_game/Adventure/status.txt", 'r') as f:
            data = json.load(f)
            f.close()
    if data == 0:
        print('Number 0 found, stopping...')
def logs():
    logs = ["Logs","Oak_Logs","Willow_Logs","Teak_Logs","Maple_Logs","Bark","Mahogany_Logs","Arctic_Pine_Logs","Yew_Logs","Sulliusceps","Magic_Logs","Redwood_Logs","Elder_Logs"]
    time.sleep(1)
    os.system('clear')
def cutChoiceLogs():
    with open("stats.json", 'r') as f:
            data = json.load(f)
            f.close()
    level = data['woodcutting level']
    woodcuttingXp = data['woodcutting xp']
    levelChecker()
    cutChoice = input("What kind of trees you would want to cut? Here are your possibilities: 1. Logs (1), 2. Oak (15), 3. Willow (30), 4. Teak (35), 5. Maple (45), 6. Bark (45), 7. Mahogany (50), 8. Arctic (54), 9. Yew (60), 10. Sulliusceps (65), 11. Magic (75), 12. Redwood (90), 13. Elder (105)\n")
    if cutChoice == "1":
        logType = Trees.NormalTree
        print("You have selected", logType.name,"... Here some info about it")
        print("Name - ", logType.name)
        print("XP - ", logType.xp)
        print("Level - ", logType.level)
        print("Loot - ", logType.loot)
        print("Time per a cut - ", logType.time, "seconds")
        cutState(logType, woodcuttingXp)
        levelChecker()
        return logType
    elif cutChoice == "2":
        logType = Trees.OakTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "3":
        logType = Trees.WillowTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "4":
        logType = Trees.TeakTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "5":
        logType = Trees.MapleTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "6":
        logType = Trees.BarkTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "7":
        logType = Trees.MahoganyTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "8":
        logType = Trees.ArcticTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "9":
        logType = Trees.YewTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "10":
        logType = Trees.SulliuscepsTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "11":
        logType = Trees.MagicTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "12":
        logType = Trees.RedwoodTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "13":
        logType = Trees.ElderTree
        if logType.level > level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level", logType.level, "Your Woodcutting level is currently", level)
            cutChoiceLogs()
        else:
            print("You have selected", logType.name,"... Here some info about it")
            print("Name - ", logType.name)
            print("XP - ", logType.xp)
            print("Level - ", logType.level)
            print("Loot - ", logType.loot)
            print("Time per a cut - ", logType.time, "seconds")
            cutState(logType, woodcuttingXp)
            levelChecker()
            return logType
    elif cutChoice == "hacks":
        LootTable.addItemToBank(Trees.NormalTree.loot_name, 1)
        LootTable.addItemToBank(Trees.OakTree.loot_name, 1)
        LootTable.addItemToBank(Trees.WillowTree.loot_name, 1)
        LootTable.addItemToBank(Trees.TeakTree.loot_name, 1)
        LootTable.addItemToBank(Trees.MapleTree.loot_name, 1)
        LootTable.addItemToBank(Trees.MapleTree.loot_name, 1)
        LootTable.addItemToBank(Trees.MapleTree.loot_name, 1)
        LootTable.addItemToBank(Trees.BarkTree.loot_name, 1)
        LootTable.addItemToBank(Trees.MahoganyTree.loot_name, 1)
        LootTable.addItemToBank(Trees.ArcticTree.loot_name, 1)
        LootTable.addItemToBank(Trees.YewTree.loot_name, 1)
        LootTable.addItemToBank(Trees.SulliuscepsTree.loot_name, 1)
        LootTable.addItemToBank(Trees.MagicTree.loot_name, 1)
        LootTable.addItemToBank(Trees.RedwoodTree.loot_name, 1)
        LootTable.addItemToBank(Trees.ElderTree.loot_name, 1)
        cutChoiceLogs()
    else:
        time.sleep(1)
        os.system('clear')
        cutChoiceLogs()


        
def cutState(logType, woodcuttingXp):
    '''
    with open("/home/linux/Documents/Python/Adventure_project/status.txt", 'r') as f:
        data = json.load(f)
        f.close()
    if data == 0:
        print('Number 0 found, stopping...')
        quit()
    
    while data != 0:
''' 
    with open("bank.json", "r") as f:
        data = json.load(f)
        f.close()
    with open("stats.json", 'r') as f:
        level2 = json.load(f)
        f.close()
    if axes["Crystal axe"]["name"] in data and level2['woodcutting level'] >= axes["Crystal axe"]["level"]:
        current_axe = axes["Crystal axe"]
    else:
        if axes["3rd age axe"]["name"] in data and level2['woodcutting level'] >= axes["3rd age axe"]["level"]:
            current_axe = axes["3rd age axe"]
        else:
            if axes["Infernal axe"]["name"] in data and level2['woodcutting level'] >= axes["Infernal axe"]["level"]:
                current_axe = axes["Infernal axe"]
            else:
                if axes["Dragon axe"]["name"] in data and level2['woodcutting level'] >= axes["Dragon axe"]["level"]:
                    current_axe = axes["Dragon axe"]
                else:
                    if axes["Rune axe"]["name"] in data and level2['woodcutting level'] >= axes["Rune axe"]["level"]:
                        current_axe = axes["Rune axe"]
                    else:
                        if axes["Adamant axe"]["name"] in data and level2['woodcutting level'] >= axes["Adamant axe"]["level"]:
                            current_axe = axes["Adamant axe"]
                        else:
                            if axes["Mithril axe"]["name"] in data and level2['woodcutting level'] >= axes["Mithril axe"]["level"]:
                                current_axe = axes["Mithril axe"]
                            else:
                                if axes["Black axe"]["name"] in data and level2['woodcutting level'] >= axes["Black axe"]["level"]:
                                    current_axe = axes["Black axe"]
                                else:
                                    if axes["Steel axe"]["name"] in data and level2['woodcutting level'] >= axes["Steel axe"]["level"]:
                                        current_axe = axes["Steel axe"]
                                    else:
                                        if axes["Iron axe"]["name"] in data and level2['woodcutting level'] >= axes["Iron axe"]["level"]:
                                            current_axe = axes["Iron axe"]
                                        else:
                                            if axes["Bronze axe"]["name"] in data and level2['woodcutting level'] >= axes["Bronze axe"]["level"]:
                                                current_axe = axes["Bronze axe"]
                                            else:
                                                current_axe = None
    if current_axe != None:
        time.sleep(logType.time * current_axe["reduction"])
        os.system('clear')   
        print("############## YOU ARE CHOPPING THE LOGS", current_axe["reduction_number"], "%", "FASTER BECAUSE OF YOUR", current_axe["name"], "##############")
        print("You managed to get 1", logType.loot_name)
        print("You gained", logType.xp, "XP")
        with open("stats.json", "r") as f:
            data = json.load(f)
            f.close()
        woodcuttingXp = data['woodcutting xp']
        woodcuttingXp = int(woodcuttingXp) + logType.xp
        woodcuttingLevel = data['woodcutting level']
        print("You have now", float(woodcuttingXp), "in Woodcutting skill. Level is:", int(woodcuttingLevel))
        print(f"{levels[int(woodcuttingLevel)] - int(woodcuttingXp)} xp remaining for next level:", woodcuttingLevel + 1)
        print(f"You have to chop: {(levels[int(woodcuttingLevel)] - int(woodcuttingXp)) / logType.xp} logs.")
        LootTable.addItemToBank(logType.loot_name, logType.amount)
        LootTable.checkItemFromBank(logType.loot_name, logType.amount)

        print(f"Banked the logs into your bank. Currently you have:{LootTable.checkItemFromBank(logType.loot_name, logType.amount)}")
        xpChecker(logType)
        levelChecker()
        cutState(logType, woodcuttingXp)
        return woodcuttingXp
    if current_axe == None:
        time.sleep(logType.time)
        os.system('clear') 
        print("You managed to get 1", logType.loot_name)
        print("You gained", logType.xp, "XP")
        with open("stats.json", "r") as f:
            data = json.load(f)
            f.close()
        woodcuttingXp = data['woodcutting xp']
        woodcuttingXp = int(woodcuttingXp) + logType.xp
        woodcuttingLevel = data['woodcutting level']
        print("You have now", float(woodcuttingXp), "in Woodcutting skill. Level is:", int(woodcuttingLevel))
        if (f"{levels[int(woodcuttingLevel)] - int(woodcuttingXp)}") > str(0):    
            print(f"{levels[int(woodcuttingLevel)] - int(woodcuttingXp)} xp remaining for next level:", woodcuttingLevel + 1)
        else:
            print("0 xp remaining for next level:", woodcuttingLevel + 1)
        print(f"You have to chop: {math.ceil((levels[int(woodcuttingLevel)] - int(woodcuttingXp)) / logType.xp)} logs.")
        LootTable.addItemToBank(logType.loot_name, logType.amount)
        LootTable.checkItemFromBank(logType.loot_name, logType.amount)

        print(f"Banked the logs into your bank. Currently you have:{LootTable.checkItemFromBank(logType.loot_name, logType.amount)}")
        xpChecker(logType)
        levelChecker()
        cutState(logType, woodcuttingXp)
        return woodcuttingXp
    
def xpChecker(logType):
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    data['woodcutting xp'] = int(data['woodcutting xp']) + logType.xp
    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()




def levelChecker():
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    woodcuttingXp = data['woodcutting xp']
    woodcuttingLevel = data['woodcutting level']
    if int(woodcuttingXp) >= levels[int(woodcuttingLevel)]:
            data['woodcutting level'] = int(data['woodcutting level']) + 1
            print(f"You got a new level! Current level is: {int(woodcuttingLevel) + 1} ")
    with open("stats.json", 'w') as f:
        data = json.dump(data, f, indent=4)
        f.close()


time.sleep(1)
os.system('clear')
#cutChoiceLogs()
