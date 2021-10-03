import random
import math
import json
import time
import numpy
import os

import LootTable

levels = [0,83,174,276,388,512,650,801,969,1154,1358,1584,1833,2107,2411,2746,3115,3523,3973,4470,5018,5624,6291,7028,7842,8740,9730,10824,12031,13363,14833,16456,18247,20224,22406,24815,27473,30408,33648,37224,41171,45529,50339,55649,61512,67983,75127,83014,91721,101333,111945,123660,136594,150872,166636,184040,203254,224466,247886,273742,302288,333804,368599,407015,449428,496254,547953,605032,668051,737627,814445,899257,992895,1096278,1210421,1336443,1475581,1629200,1798808,1986068,2192818,2421087,2673114,2951373,3258594,3597792,3972294,4385776,4842295,5346332,5902831,6517253,7195629,7944614,8771558,9684577,10692629,11805606,13034431,14391160,15889109,17542976,19368992,21385073,23611006,26068632,28782069,31777943,35085654,38737661,42769801,47221641,52136869,57563718,63555443,70170840,77474828,85539082,94442737,104273167,115126838,127110260,140341028,154948977,171077457,188884740]
class Bars(object):
    class BronzeBar(object):
        name = "Bronze bar"
        xp = 6.2
        level = 1
        supply_1 = "Tin ore"
        supply_1_amount = 1
        supply_2 = "Copper ore"
        supply_2_amount = 1
        loot_name = "Bronze bar"
        time = 1
        amount = 1    
    class BluriteBar(object):
        name = "Blurite bar"
        xp = 8
        bar_xp = 17.5
        level = 8
        supply_1 = "Blurite ore"
        supply_1_amount = 1
        loot_name = "Blurite bar"
        time = 1
        amount = 1
    class IronBar(object):
        name = "Iron bar"
        xp = 12.5
        bar_xp = 25
        level = 15
        supply_1 = "Iron ore"
        supply_1_amount = 1
        loot_name = "Iron bar"
        time = 1
        amount = 1
    class SilverBar(object):
        name = "Silver bar"
        xp = 13.7
        level = 20
        supply_1 = "Silver ore"
        supply_1_amount = 1
        loot_name = "Silver bar"
        time = 1
        amount = 1
    class SteelBar(object):
        name = "Steel bar"
        xp = 17.5
        bar_xp = 37.5
        level = 30
        supply_1 = "Iron ore"
        supply_1_amount = 1
        supply_2 = "Coal"
        supply_2_amount = 1
        loot_name = "Steel bar"
        time = 1
        amount = 1
    class GoldBar(object):
        with open('bank.json') as f:
            data = json.load(f)
            f.close()
        if data['Goldsmith gauntlets']['quantity'] > 0:
            name = "Gold bar"
            xp = 56.2
            level = 40
            supply_1 = "Gold ore"
            supply_1_amount = 1
            supply_2 = None
            loot_name = "Gold bar"
            time = 1
            amount = 1

        else:
            name = "Gold bar"
            xp = 22.5
            level = 40
            supply_1 = "Gold ore"
            supply_1_amount = 1
            supply_2 = None
            loot_name = "Gold bar"
            time = 1
            amount = 1

    class MithrilBar(object):
        name = "Mithril bar"
        xp = 30
        bar_xp = 50 
        level = 50
        loot_used = "Tin ore", "Copper ore"
        loot_name = "Bronze bar"
        time = 1
        amount = 1
    class AdamantBar(object):
        name = "Adamant bar"
        xp = 37.5
        bar_xp = 62.5
        level = 70
        supply_1 = "Adamantite ore"
        supply_1_amount = 1
        supply_2 = "Coal"
        supply_2_amount = 6
        loot_name = "Adamant bar"
        time = 1
        amount = 1
    class RuniteBar(object):
        name = "Runite bar"
        xp = 50
        bar_xp = 75
        level = 85
        supply_1 = "Runite ore"
        supply_1_amount = 1
        supply_2 = "Coal"
        supply_2_amount = 8
        loot_name = "Runite bar"
        time = 1
        amount = 1

class Bronze(object):
    class Dagger(object):
        name = "Bronze dagger"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze dagger"
        time = 1
        amount = 1
    class Axe(object):
        name = "Bronze axe"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze axe"
        time = 1
        amount = 1
    class Mace(object):
        name = "Bronze mace"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 2
        material_used = "Bronze bar"
        loot_name = "Bronze mace"
        time = 1
        amount = 1
    class Mace(object):
        name = "Bronze mace"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze mace"
        time = 1
        amount = 1
    class MedHelm(object):
        name = "Bronze med helm"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze med helm"
        time = 1
        amount = 1
    class UnfinishedBolts(object):
        name = "Bronze unfinished bolts"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze unfinished bolts"
        time = 1
        amount = 10
    class Sword(object):
        name = "Bronze sword"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze sword"
        time = 1
        amount = 1
    class DartTip(object):
        name = "Bronze dart tip"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze dart tip"
        time = 1
        amount = 10
    class Wire(object):
        name = "Bronze wire"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze wire"
        time = 1
        amount = 1
    class Nails(object):
        name = "Bronze nails"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze nails"
        time = 1
        amount = 15
    class Scimitar(object):
        name = "Bronze scimitar"
        bars_used = 2
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze scimitar"
        time = 1
        amount = 1
    class Spear(object):
        name = "Bronze spear"
        bars_used = 1
        second_material = "Logs"
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze spear"
        time = 1
        amount = 1
    class Hasta(object):
        name = "Bronze hasta"
        bars_used = 1
        second_material = "Logs"
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze hasta"
        time = 1
        amount = 1
    class Arrowtips(object):
        name = "Bronze arrowtips"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze arrowtips"
        time = 1
        amount = 15
    class CrossbowLimbs(object):
        name = "Bronze crossbow limbs"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze crossbow limbs"
        time = 1
        amount = 1
    class Longsword(object):
        name = "Bronze longsword"
        bars_used = 2
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze longsword"
        time = 1
        amount = 1
    class JavelinHeads(object):
        name = "Bronze javelin heads"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze javelin heads"
        time = 1
        amount = 5
    class FullHelm(object):
        name = "Bronze full helm"
        bars_used = 2
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze full helm"
        time = 1
        amount = 1
    class ThrowingKnife(object):
        name = "Bronze throwing knife"
        bars_used = 1
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze throwing knife"
        time = 1
        amount = 5
    class SqShield(object):
        name = "Bronze sq shield"
        bars_used = 2
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze sq shield"
        time = 1
        amount = 1
    class Warhammer(object):
        name = "Bronze warhammer"
        bars_used = 3
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze warhammer"
        time = 1
        amount = 1
    class Battleaxe(object):
        name = "Bronze battleaxe"
        bars_used = 3
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze battleaxe"
        time = 1
        amount = 1
    class Chainbody(object):
        name = "Bronze chainbody"
        bars_used = 3
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze chainbody"
        time = 1
        amount = 1
    class Kiteshield(object):
        name = "Bronze kiteshield"
        bars_used = 3
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze arrowtips"
        time = 1
        amount = 1
    class Claws(object):
        name = "Bronze claws"
        bars_used = 2
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze claws"
        time = 1
        amount = 1
    class TwoHandedSword(object):
        name = "Bronze 2h sword"
        bars_used = 3
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze 2h sword"
        time = 1
        amount = 1
    class Platelegs(object):
        name = "Bronze platelegs"
        bars_used = 3
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze platelegs"
        time = 1
        amount = 1
    class Plateskirt(object):
        name = "Bronze plateskirt"
        bars_used = 3
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze plateskirt"
        time = 1
        amount = 1
    class Platebody(object):
        name = "Bronze platebody"
        bars_used = 5
        xp = bars_used * Bars.BronzeBar.bar_xp
        level = 1
        material_used = "Bronze bar"
        loot_name = "Bronze platebody"
        time = 1
        amount = 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def smeltChoice():
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    smithingLevel = data['smithing level']
    smithingXp = data['smithing xp']
    levelChecker()
    os.system("clear")
    smelt_input = input("What would you like to smelt? Here are your possibilities: 1. Bronze (1), 2. Blurite (8), 3. Iron (15), 4. Silver (20), 5. Steel (30), 6. Gold (40), 7. Mithril (50), \n 8. Adamant (70), 9. Runite (85)\n")
    if smelt_input == "1":
        SmeltType = Bars.BronzeBar
        os.system('clear')
        print("You have selected", SmeltType.name,"... Here some info about it")
        print("Name - ", SmeltType.name)
        print("XP - ", SmeltType.xp)
        print("Level - ", SmeltType.level)
        print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1} and {SmeltType.supply_2_amount} {SmeltType.supply_2}")
        print("Loot - ", SmeltType.loot_name)
        print("Time per a smelt - ", SmeltType.time, "seconds")
        input("Press enter to continue")
        smeltState(SmeltType, smithingXp)
        levelChecker()
        return SmeltType
    elif smelt_input == "2":
        SmeltType = Bars.BluriteBar
        if smithingLevel > SmeltType.level:
            os.system('clear')
            print("You have selected", SmeltType.name,"... Here some info about it")
            print("Name - ", SmeltType.name)
            print("XP - ", SmeltType.xp)
            print("Level - ", SmeltType.level)
            print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1}")
            print("Loot - ", SmeltType.loot_name)
            print("Time per a smelt - ", SmeltType.time, "seconds")
            input("Press enter to continue")
            smeltState(SmeltType, smithingXp)
            levelChecker()
        else:
            print(f"Your Smithing level is not high enough to smelt {SmeltType.name}. You need to get level {SmeltType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
            input("Press enter to continue")
            smeltChoice()
    elif smelt_input == "3":
        SmeltType = Bars.IronBar
        if smithingLevel > SmeltType.level:
            os.system('clear')
            print("You have selected", SmeltType.name,"... Here some info about it")
            print("Name - ", SmeltType.name)
            print("XP - ", SmeltType.xp)
            print("Level - ", SmeltType.level)
            print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1}")
            print("Loot - ", SmeltType.loot_name)
            print("Time per a smelt - ", SmeltType.time, "seconds")
            input("Press enter to continue")
            smeltState(SmeltType, smithingXp)
            levelChecker()
        else:
            print(f"Your Smithing level is not high enough to smelt {SmeltType.name}. You need to get level {SmeltType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
            input("Press enter to continue")
            smeltChoice()
    elif smelt_input == "4":
        SmeltType = Bars.SilverBar
        if smithingLevel > SmeltType.level:
            os.system('clear')
            print("You have selected", SmeltType.name,"... Here some info about it")
            print("Name - ", SmeltType.name)
            print("XP - ", SmeltType.xp)
            print("Level - ", SmeltType.level)
            print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1}")
            print("Loot - ", SmeltType.loot_name)
            print("Time per a smelt - ", SmeltType.time, "seconds")
            input("Press enter to continue")
            smeltState(SmeltType, smithingXp)
            levelChecker()
        else:
            print(f"Your Smithing level is not high enough to smelt {SmeltType.name}. You need to get level {SmeltType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
            input("Press enter to continue")
            smeltChoice()
    elif smelt_input == "5":
        SmeltType = Bars.SteelBar
        if smithingLevel > SmeltType.level:            
            os.system('clear')
            print("You have selected", SmeltType.name,"... Here some info about it")
            print("Name - ", SmeltType.name)
            print("XP - ", SmeltType.xp)
            print("Level - ", SmeltType.level)
            print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1} and {SmeltType.supply_2_amount} {SmeltType.supply_2}")
            print("Loot - ", SmeltType.loot_name)
            print("Time per a smelt - ", SmeltType.time, "seconds")
            input("Press enter to continue")
            smeltState(SmeltType, smithingXp)
            levelChecker()
        else:
            print(f"Your Smithing level is not high enough to smelt {SmeltType.name}. You need to get level {SmeltType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
            input("Press enter to continue")
            smeltChoice()
    elif smelt_input == "6":
        SmeltType = Bars.GoldBar
        with open('bank.json') as f:
            data = json.load(f)
            f.close()
        if smithingLevel > SmeltType.level:
            os.system('clear')
            print("You have selected", SmeltType.name,"... Here some info about it")
            print("Name - ", SmeltType.name)
            print("XP - ", SmeltType.xp)
            print("Level - ", SmeltType.level)
            print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1}")
            print("Loot - ", SmeltType.loot_name)
            print("Time per a smelt - ", SmeltType.time, "seconds")
            input("Press enter to continue")
            smeltState(SmeltType, smithingXp)
            levelChecker()            
        else:
            print(f"Your Smithing level is not high enough to smelt {SmeltType.name}. You need to get level {SmeltType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
            input("Press enter to continue")
            smeltChoice()
    elif smelt_input == "7":
        SmeltType = Bars.MithrilBar
        if smithingLevel > SmeltType.level:
            os.system('clear')
            print("You have selected", SmeltType.name,"... Here some info about it")
            print("Name - ", SmeltType.name)
            print("XP - ", SmeltType.xp)
            print("Level - ", SmeltType.level)
            print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1} and {SmeltType.supply_2_amount} {SmeltType.supply_2}")
            print("Loot - ", SmeltType.loot_name)
            print("Time per a smelt - ", SmeltType.time, "seconds")
            input("Press enter to continue")
            smeltState(SmeltType, smithingXp)
            levelChecker()
        else:
            print(f"Your Smithing level is not high enough to smelt {SmeltType.name}. You need to get level {SmeltType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
            input("Press enter to continue")
            smeltChoice()
    elif smelt_input == "8":
        SmeltType = Bars.AdamantBar
        if smithingLevel > SmeltType.level:
            os.system('clear')
            print("You have selected", SmeltType.name,"... Here some info about it")
            print("Name - ", SmeltType.name)
            print("XP - ", SmeltType.xp)
            print("Level - ", SmeltType.level)
            print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1} and {SmeltType.supply_2_amount} {SmeltType.supply_2}")
            print("Loot - ", SmeltType.loot_name)
            print("Time per a smelt - ", SmeltType.time, "seconds")
            input("Press enter to continue")
            smeltState(SmeltType, smithingXp)
            levelChecker()
        else:
            print(f"Your Smithing level is not high enough to smelt {SmeltType.name}. You need to get level {SmeltType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
            input("Press enter to continue")
            smeltChoice()            
    elif smelt_input == "9":
        SmeltType = Bars.RuniteBar
        if smithingLevel > SmeltType.level:
            os.system('clear')
            print("You have selected", SmeltType.name,"... Here some info about it")
            print("Name - ", SmeltType.name)
            print("XP - ", SmeltType.xp)
            print("Level - ", SmeltType.level)
            print(f"You need - {SmeltType.supply_1_amount} {SmeltType.supply_1}")
            print("Loot - ", SmeltType.loot_name)
            print("Time per a smelt - ", SmeltType.time, "seconds")
            input("Press enter to continue")
            smeltState(SmeltType, smithingXp)
            levelChecker()
        else:
            print(f"Your Smithing level is not high enough to smelt {SmeltType.name}. You need to get level {SmeltType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
            input("Press enter to continue")
            smeltChoice()            
    else:
        smeltChoice()

def smeltState(SmeltType, smithingXp):
    time.sleep(2)
    os.system('clear')
    with open("bank.json", "r") as f:
        bank_data = json.load(f)
        f.close()
    with open("stats.json", "r") as f:
        data = json.load(f)
        f.close()
    smithingXp = data['smithing xp']
    smithingLevel = data['smithing level']
    time.sleep(SmeltType.time)
    if SmeltType == Bars.GoldBar or SmeltType == Bars.SilverBar or SmeltType == Bars.IronBar or SmeltType == Bars.BluriteBar:
        ore_1 = bank_data[SmeltType.supply_1]['quantity']
        if ore_1 > SmeltType.supply_1_amount:
            print(LootTable.checkItemFromBank(SmeltType.supply_1, 0))
            print(f"You got {SmeltType.xp} xp.")
            print("You have now", float(smithingXp), "in Smithing skill. Level is:", int(smithingLevel))
            if (f"{levels[int(smithingLevel)] - int(smithingXp)}") >= str(0):    
                print(f"{levels[int(smithingLevel)] - int(smithingXp)} xp remaining for next level:", smithingLevel + 1)
            else:
                print("0 xp remaining for next level:", smithingLevel + 1)        
            print(f"You have to smelt: {math.ceil((levels[int(smithingLevel)] - int(smithingXp)) / SmeltType.xp)} bars.")
        else:
            print("You don't have enough resources to smelt these. Heading back to smelt-menu.")
            input("Press enter to continue")
            smeltChoice()
    else:
        ore_1 = bank_data[SmeltType.supply_1]['quantity']
        ore_2 = bank_data[SmeltType.supply_2]['quantity']
        if ore_1 > SmeltType.supply_1_amount and ore_2 > SmeltType.supply_2_amount:
            print(LootTable.checkItemFromBank(SmeltType.supply_1, 0))
            print(f"You got {SmeltType.xp} xp.")
            print("You have now", float(smithingXp), "in Smithing skill. Level is:", int(smithingLevel))
            if (f"{levels[int(smithingLevel)] - int(smithingXp)}") >= str(0):    
                print(f"{levels[int(smithingLevel)] - int(smithingXp)} xp remaining for next level:", smithingLevel + 1)
            else:
                print("0 xp remaining for next level:", smithingLevel + 1)        
            print(f"You have to smelt: {math.ceil((levels[int(smithingLevel)] - int(smithingXp)) / SmeltType.xp)} bars.")
        else:
            print("You don't have enough resources to smelt these. Heading back to smelt-menu.")
            input("Press enter to continue")
            smeltChoice()
    
def smithChoice():
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    smithingLevel = data['smithing level']
    smithingXp = data['smithing xp']
    levelChecker()
    os.system("clear")
    smith_input = input("What kind of bars would you like to smith? Here are your possibilities: 1. Bronze (1), 2. Blurite (8), 3. Iron (15), 4. Silver (20), 5. Steel (30), 6. Gold (40), 7. Mithril (50), \n 8. Adamant (70), 9. Runite (85) \n")
    if smith_input == "1":
        SmithType = Bars.BronzeBar
        print("You have selected", SmithType.name,"... Here some info about it")
        print("Name - ", SmithType.name)
        print("XP - ", SmithType.xp)
        print("Level - ", SmithType.level)
        print("Loot - ", SmithType.loot_name)
        print("Time per a smelt - ", SmithType.time, "seconds")
        smithState(SmithType, smithingXp)
        levelChecker()
        return SmithType
    elif smith_input == "2":
        SmithType = Bars.BluriteBar
        if smithingLevel > SmithType.level:
            print("You have selected", SmithType.name,"... Here some info about it")
            print("Name - ", SmithType.name)
            print("XP - ", SmithType.xp)
            print("Level - ", SmithType.level)
            print("Loot - ", SmithType.loot_name)
            print("Time per a smelt - ", SmithType.time, "seconds")
            smithState(SmithType, smithingXp)
            levelChecker()
        else:
            print(f"Your Smithing level is not high enough to smelt {SmithType.name}. You need to get level {SmithType.level} Smithing. Your Smithing level is currently: {smithingLevel}")
    elif smith_input == "3":
        SmithType = Bars.IronBar
        print("You have selected", SmithType.name,"... Here some info about it")
        print("Name - ", SmithType.name)
        print("XP - ", SmithType.xp)
        print("Level - ", SmithType.level)
        print("Loot - ", SmithType.loot_name)
        print("Time per a smelt - ", SmithType.time, "seconds")
        smithState(SmithType, smithingXp)
        levelChecker()
    elif smith_input == "4":
        SmithType = Bars.SteelBar
        print("You have selected", SmithType.name,"... Here some info about it")
        print("Name - ", SmithType.name)
        print("XP - ", SmithType.xp)
        print("Level - ", SmithType.level)
        print("Loot - ", SmithType.loot_name)
        print("Time per a smelt - ", SmithType.time, "seconds")
        smithState(SmithType, smithingXp)
        levelChecker()
    elif smith_input == "5":
        SmithType = Bars.IronBar
        print("You have selected", SmithType.name,"... Here some info about it")
        print("Name - ", SmithType.name)
        print("XP - ", SmithType.xp)
        print("Level - ", SmithType.level)
        print("Loot - ", SmithType.loot_name)
        print("Time per a smelt - ", SmithType.time, "seconds")
        smithState(SmithType, smithingXp)
        levelChecker()
    else:
        smithChoice()

def smithState(SmithType, smithingXp):
    with open("bank.json", "r") as f:
        data = json.load(f)
        f.close()


def xpChecker(SmithType):
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    data['smithing xp'] = int(data['smithing xp']) + SmithType.xp
    data['total xp'] = int(data['total xp']) + SmithType.xp
    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()




def levelChecker():
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    smithingXp = data['smithing xp']
    smithingLevel = data['smithing level']
    if int(smithingXp) >= levels[int(smithingLevel)]:
        data['smithing level'] = int(data['smithing level']) + 1
        data['total level'] = int(data['total level']) + 1
        print(f"You got a new level! Current level is: {int(smithingLevel) + 1} ")
    with open("stats.json", 'w') as f:
        data = json.dump(data, f, indent=4)
        f.close()

