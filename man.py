import random
import numpy

class quantity():
    water_rune = 7
    earth_rune = 4
    fire_rune = 6
    mind_rune = 9
    chaos_rune = 2
    body_rune = 7
    grimy_guam = 1
    grimy_marrentill = 1
    grimy_tarromin = 1
    frimy_harralander = 1
    grimy_ranarr = 1
    grimy_kwuarm = 1
    grimy_irit = 1
    grimy_avantoe = 1
    grimy_cadantine = 1
    grimy_dwarfe_weed = 1
    chargebow = 1
    bronze_bolts = 2, 12
    bronze_arrow = 7
    tiny_spiky_iron_salvage = 1
    tiny_plated_bronze_salvage = 1
    staff_of_air = 1
    air_talisman = 1
    earth_talisman = 1
    cabbage = 1
    fishing_bait = 1
    copper_stone_spirit = 1
    tin_stone_spirit = 1
    coins = 1, 40
    sealed_clue_scroll_easy = 1
    key_token = 1
    mimic_kill_token = 1


water_rune = 0
earth_rune = 0
fire_rune = 0
mind_rune = 0
chaos_rune = 0
body_rune = 0
grimy_guam = 0
grimy_marrentill = 0
grimy_tarromin = 0
frimy_harralander = 0
grimy_ranarr = 0
grimy_kwuarm = 0
grimy_irit = 0
grimy_avantoe = 0
grimy_cadantine = 0
grimy_dwarfe_weed = 0
chargebow = 0
bronze_bolts = 0
bronze_arrow = 0
tiny_spiky_iron_salvage = 0
tiny_plated_bronze_salvage = 0
staff_of_air = 0
air_talisman = 0
earth_talisman = 0
cabbage = 0
fishing_bait = 0
copper_stone_spirit = 0
tin_stone_spirit = 0
coins = 0
sealed_clue_scroll_easy = 0
key_token = 0
mimic_kill_token = 0


#rngnumber = random.randint(1, 5000)
itemrates = "common", "uncommon", "rare", "very rare"
probabilities = ["0.5", "0.35", "0.1", "0.05"]
testnumber = 10
for x in range(testnumber):
    #print(numpy.random.choice(itemrates, p=probabilities))
    if numpy.random.choice(itemrates, p=probabilities) == "common":
        a = random.randint(1, 4)
        if a == 1:
            grimy_guam = grimy_guam + quantity.grimy_guam
        if a == 2:
            chargebow = chargebow + quantity.chargebow
        if a == 3:
            bronze_bolts = bronze_bolts + random.randint(2, 12)
        if a == 4:
            coins = coins + random.randint(1, 40)
    print("Guam", grimy_guam, "Chargebow""              ", chargebow, "Bronze bolts", "               ", bronze_bolts, "coins","            ", coins)
            
