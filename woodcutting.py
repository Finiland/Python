import random
import math
import json
import time
import os


levels = [0,83,174,276,388,512,650,801,969,1154,1358,1584,1833,2107,2411,2746,3115,3523,3973,4470,5018,5624,6291,7028,7842,8740,9730,10824,12031,13363,14833,16456,18247,20224,22406,24815,27473,30408,33648,37224,41171,45529,50339,55649,61512,67983,75127,83014,91721,101333,111945,123660,136594,150872,166636,184040,203254,224466,247886,273742,302288,333804,368599,407015,449428,496254,547953,605032,668051,737627,814445,899257,992895,1096278,1210421,1336443,1475581,1629200,1798808,1986068,2192818,2421087,2673114,2951373,3258594,3597792,3972294,4385776,4842295,5346332,5902831,6517253,7195629,7944614,8771558,9684577,10692629,11805606,13034431,14391160,15889109,17542976,19368992,21385073,23611006,26068632,28782069,31777943,35085654,38737661,42769801,47221641,52136869,57563718,63555443,70170840,77474828,85539082,94442737,104273167,115126838,127110260,140341028,154948977,171077457,188884740]



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
        loot_name = "Oak Logs"
        time = 1.2
        amount = 1
    class WillowTree(object):
        name = "Willow"
        xp = 67.5
        level = 30
        loot = "Willow_Logs"
        loot_name = "Willow Logs"
        time = 1.4
        amount = 1
    class TeakTree(object):
        name = "Teak"
        xp = 85
        level = 35
        loot = "Teak_Logs"
        loot_name = "Teak Logs"
        time = 1.6
        amount = 1
    class MapleTree(object):
        name = "Maple"
        xp = 100
        level = 45
        loot = "Maple_Logs"
        loot_name = "Maple Logs"
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
        loot_name = "Mahogany Logs"
        time = 2.2
        amount = 1
    class ArcticTree(object):
        name = "Arctic pine"
        xp = 40
        level = 54
        loot = "Arctic_Pine_Logs"
        loot_name = "Arctic Pine Logs"
        time = 2.4
        amount = 1
    class YewTree(object):
        name = "Yew"
        xp = 175
        level = 60
        loot = "Yew_Logs"
        loot = "Yew Logs"
        time = 2.6
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
        loot_name = "Magic Logs"
        time = 3
        amount = 1
    class RedwoodTree(object):
        name = "Redwood"
        xp = 380
        level = 90
        loot = "Redwood_Logs"
        loot_name = "Redwood Logs"
        time = 3.2
        amount = 1
    class ElderTree(object):
        name = "Elder"
        xp = 500
        level = 105
        loot = "Elder_Logs"
        loot_name = "Elder Logs"
        time = 3.4
        amount = 1
    



def logs():
    logs = ["Logs","Oak_Logs","Willow_Logs","Teak_Logs","Maple_Logs","Bark","Mahogany_Logs","Arctic_Pine_Logs","Yew_Logs","Sulliusceps","Magic_Logs","Redwood_Logs","Elder_Logs"]
def cutChoiceLogs():
    with open("stats.json", 'r') as f:
            data = json.load(f)
            f.close()
    level = data['woodcutting level']
    woodcuttingXp = data['woodcutting xp']
    levelChecker()
    cutChoice = input("What kind of trees you would want to cut? Here are your possibilities: 1. Logs, 2. Oak, 3. Willow, 4. Teak, 5. Maple, 6. Bark, 7. Mahogany, 8. Arctic, 9. Yew, 10. Sulliusceps, 11. Magic, 12. Redwood, 13. Elder\n")
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
        if level < logType.level:
            print("Your Woodcutting level is not good enough to cut", logType.name, ". You need to get level 15 Woodcutting. Your Woodcutting level is currently", level)
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
    else:
        cutChoiceLogs()


        
def cutState(logType, woodcuttingXp):
    amountRange = 50
    #for x in range(int(1800 / logType.time)):
    for x in range(amountRange):
        amountRange = amountRange - 1
        print("You can chop this many logs still: ", amountRange)
        time.sleep(logType.time)
        os.system('clear')
        print("You managed to get 1", logType.loot_name)
        print("You gained", logType.xp, "XP")
        with open("stats.json", "r") as f:
            data = json.load(f)
            f.close()
        woodcuttingXp = data['woodcutting xp']
        woodcuttingXp = woodcuttingXp + logType.xp
        print("You have now", float(woodcuttingXp), "in Woodcutting skill")
        xpChecker(logType)
        levelChecker()
        
    
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


    if int(woodcuttingXp) >= int(levels[woodcuttingLevel]):
            data['woodcutting level'] = int(data['woodcutting level']) + 1
            print(f"You got a new level! Current level is: {woodcuttingLevel + 1} ")
    with open("stats.json", 'w') as f:
        data = json.dump(data, f, indent=4)
        f.close()



#cutChoiceLogs()
