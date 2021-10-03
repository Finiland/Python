import random
import math
import json
import time
import os


import LootTable


levels = [0,83,174,276,388,512,650,801,969,1154,1358,1584,1833,2107,2411,2746,3115,3523,3973,4470,5018,5624,6291,7028,7842,8740,9730,10824,12031,13363,14833,16456,18247,20224,22406,24815,27473,30408,33648,37224,41171,45529,50339,55649,61512,67983,75127,83014,91721,101333,111945,123660,136594,150872,166636,184040,203254,224466,247886,273742,302288,333804,368599,407015,449428,496254,547953,605032,668051,737627,814445,899257,992895,1096278,1210421,1336443,1475581,1629200,1798808,1986068,2192818,2421087,2673114,2951373,3258594,3597792,3972294,4385776,4842295,5346332,5902831,6517253,7195629,7944614,8771558,9684577,10692629,11805606,13034431,14391160,15889109,17542976,19368992,21385073,23611006,26068632,28782069,31777943,35085654,38737661,42769801,47221641,52136869,57563718,63555443,70170840,77474828,85539082,94442737,104273167,115126838,127110260,140341028,154948977,171077457,188884740]

class Logs(object):
    class NormalLogs(object):
        name = "Logs"
        xp = 40
        level = 1
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class AcheyLogs(object):
        name = "Achey logs"
        xp = 40
        level = 1
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreNormalLogs(object):
        name = "Pyre logs"
        xp = 50.5
        level = 5
        time = 1
        amount = 1
        sacred_oil_doses = 2
        alias = "logs", "Logs", "LoGs", "lOgs"
    class OakLogs(object):
        name = "Oak logs"
        xp = 60
        level = 15
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreOakLogs(object):
        name = "Oak pyre logs"
        xp = 70
        level = 20
        time = 1
        amount = 1
        sacred_oil_doses = 2
        alias = "logs", "Logs", "LoGs", "lOgs"
    class WillowLogs(object):
        name = "Willow logs"
        xp = 90
        level = 30
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreWillowLogs(object):
        name = "Willow pyre logs"
        xp = 100
        level = 35
        time = 1
        amount = 1
        sacred_oil_doses = 3
        alias = "logs", "Logs", "LoGs", "lOgs"
    class TeakLogs(object):
        name = "Teak logs"
        xp = 105
        level = 35
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class TeakLogs(object):
        name = "Teak logs"
        xp = 120
        level = 40
        time = 1
        amount = 1
        sacred_oil_doses = 3
        alias = "logs", "Logs", "LoGs", "lOgs"
    class ArcticPineLogs(object):
        name = "Arctic pine logs"
        xp = 125
        level = 42
        time = 1
        amount = 1
        sacred_oil_doses = 3
        alias = "logs", "Logs", "LoGs", "lOgs"
    class MapleLogs(object):
        name = "Maple logs"
        xp = 135
        level = 45
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreArcticLogs(object):
        name = "Arctic pyre logs"
        xp = 158
        level = 47
        time = 1
        amount = 1
        sacred_oil_doses = 3
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreMapleLogs(object):
        name = "Maple pyre logs"
        xp = 175
        level = 50
        time = 1
        amount = 1
        sacred_oil_doses = 3
        alias = "logs", "Logs", "LoGs", "lOgs"
    class MahoganyLogs(object):
        name = "Mahogany logs"
        xp = 157.5
        level = 50
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreMahoganyLogs(object):
        name = "Mahogany pyre logs"
        xp = 210
        level = 55
        time = 1
        amount = 1
        sacred_oil_doses = 3
        alias = "logs", "Logs", "LoGs", "lOgs"
    class YewLogs(object):
        name = "Yew logs"
        xp = 202.5
        level = 60
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class BlisterwoodLogs(object):
        name = "Blisterwood logs"
        xp = 96
        level = 62
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreYewLogs(object):
        name = "Yew pyre logs"
        xp = 225
        level = 65
        time = 1
        amount = 1
        sacred_oil_doses = 4
        alias = "logs", "Logs", "LoGs", "lOgs"
    class MagicLogs(object):
        name = "Magic logs"
        xp = 303.8
        level = 75
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreMagicLogs(object):
        name = "Magic pyre logs"
        xp = 404.5
        level = 80
        time = 1
        amount = 1
        sacred_oil_doses = 4
        alias = "logs", "Logs", "LoGs", "lOgs"
    class RedwoodLogs(object):
        name = "Redwood logs"
        xp = 350
        level = 90
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreRedwoodLogs(object):
        name = "Redwood pyre logs"
        xp = 500
        level = 95
        time = 1
        amount = 1
        sacred_oil_doses = 4
        alias = "logs", "Logs", "LoGs", "lOgs"
    class ElderLogs(object):
        name = "Elder logs"
        xp = 600
        level = 105
        time = 1
        amount = 1
        alias = "logs", "Logs", "LoGs", "lOgs"
    class PyreElderLogs(object):
        name = "Elder pyre logs"
        xp = 800
        level = 108
        time = 1
        amount = 1
        sacred_oil_doses = 6
        alias = "logs", "Logs", "LoGs", "lOgs"


def xpChecker(LightLogs):
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    data['firemaking xp'] = int(data['firemaking xp']) + LightLogs.xp
    data['total xp'] = int(data['total xp']) + LightLogs.xp
    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()

def lightChoiceLogs():
    with open("stats.json", 'r') as f:
            data = json.load(f)
            f.close()
    level = data['firemaking level']
    firemakingXp = data['firemaking xp']
    levelChecker()
    lightChoice = input("What kind of logs would you want to light? Here are your possibilities: 1. Logs (1), 2. Achey logs (1), 3. Oak logs (15), 4. Willow logs (30), 5. Teak logs (35) \n 6. Maple logs (45), 7. Mahogany logs (50), 8. Yew logs(60), 9. Blisterwood logs (62), 10. Magic logs (75), 11. Redwood logs (90), 12. Elder logs (105)")
    if lightChoice == "1":
        LightLogs = Logs.NormalLogs
        print("You have selected", LightLogs.name,"... Here some info about it")
        print("Name - ", LightLogs.name)
        print("XP - ", LightLogs.xp)
        print("Level - ", LightLogs.level)
        print("Time per a light - ", LightLogs.time, "seconds")
        LightState(LightLogs, firemakingXp)
        levelChecker()
        return LightLogs
    elif lightChoice == "2":
        LightLogs = Logs.AcheyLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "3":
        LightLogs = Logs.OakLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "4":
        LightLogs = Logs.WillowLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "5":
        LightLogs = Logs.TeakLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "6":
        LightLogs = Logs.MapleLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "7":
        LightLogs = Logs.MahoganyLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "8":
        LightLogs = Logs.YewLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "9":
        LightLogs = Logs.BlisterwoodLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "10":
        LightLogs = Logs.MagicLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "11":
        LightLogs = Logs.RedwoodLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    elif lightChoice == "12":
        LightLogs = Logs.ElderLogs
        if LightLogs.level > level:
            print("Your firemaking level is not high enough to light ", LightLogs.name, ". You need to get level", LightLogs.level, "Your Firemaking level currently:", level)
            lightChoiceLogs()
        else:
            print("You have selected", LightLogs.name,"... Here some info about it")
            print("Name - ", LightLogs.name)
            print("XP - ", LightLogs.xp)
            print("Level - ", LightLogs.level)
            print("Time per a light - ", LightLogs.time, "seconds")
            LightState(LightLogs, firemakingXp)
            levelChecker()
            return LightLogs
    else:
        print("Wrong input.")
        time.sleep(1)
        os.system('clear')
        lightChoiceLogs()

def LightState(LightLogs, firemakingXp):
    with open("bank.json", "r") as f:
        data = json.load(f)
        f.close()
        if data[f'{LightLogs.name}']['name'] and data[f'{LightLogs.name}']['quantity'] > 0:
            LootTable.minusItemFromBank(LightLogs.name, LightLogs.amount)
            time.sleep(LightLogs.time)
            os.system('clear')   
            print(f"Took {LightLogs.amount} {LightLogs.name} from your bank. You currently have:{LootTable.checkItemFromBank(LightLogs.name, LightLogs.amount)}")
            print("You managed to light 1", LightLogs.name)
            print("You gained", LightLogs.xp, "XP")
            with open("stats.json", "r") as f:
                data = json.load(f)
                f.close()
            firemakingXp = data['firemaking xp']
            firemakingXp = int(firemakingXp) + LightLogs.xp
            firemakingLevel = data['firemaking level']
            print("You have now", float(firemakingXp), "in Firemaking skill. Level is:", int(firemakingLevel))
            if (f"{levels[int(firemakingLevel)] - int(firemakingXp)}") > str(0):    
                print(f"{levels[int(firemakingLevel)] - int(firemakingXp)} xp remaining for next level:", firemakingLevel + 1)
            else:
                print("0 xp remaining for next level:", firemakingLevel + 1)        
            print(f"You have to light: {math.ceil((levels[int(firemakingLevel)] - int(firemakingXp)) / LightLogs.xp)} logs.")    
            #print(f"Banked the logs into your bank. Currently you have:{LootTable.checkItemFromBank(LightLogs.name, LightLogs.amount)}")
            xpChecker(LightLogs)
            levelChecker()
            LightState(LightLogs, firemakingXp)
            return firemakingXp
        else:
            print("You do not have that in the bank!")

def levelChecker():
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    firemakingXp = data['firemaking xp']
    firemakingLevel = data['firemaking level']
    if int(firemakingXp) >= levels[int(firemakingLevel)]:
            data['firemaking level'] = int(data['firemaking level']) + 1
            data['total level'] = int(data['total level']) + 1
            print(f"You got a new level! Current level is: {int(firemakingLevel) + 1} ")
    with open("stats.json", 'w') as f:
        data = json.dump(data, f, indent=4)
        f.close()