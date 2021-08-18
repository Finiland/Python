import random
import math
import time
import json
import woodcutting as WC






def main():
    inputteriino = input('Mitä haluat tehdä?: ')
    if inputteriino == ("start game"):
        start_game()
    elif inputteriino == ("chop"):
        WC.cutChoiceLogs()
    else:
        print('Vaihtoehdot: chop, startgame')
        main()
def start_game():
    with open("stats.json", 'r') as f:
        data = json.load(f)
        f.close()
    data['total level'] = "0"
    data['total xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['hitpoints level'] = "10"
    data['hitpoints xp'] = "1154"
    data['mining level'] = "1"
    data['mining xp'] = "0"
    data['strength level'] = "1"
    data['strength xp'] = "0"
    data['agility level'] = "1"
    data['agility xp'] = "0"
    data['smithing level'] = "1"
    data['smithing xp'] = "0"
    data['defence level'] = "1"
    data['defence xp'] = "0"
    data['herblore level'] = "1"
    data['herblore xp'] = "0"
    data['fishing level'] = "1"
    data['fishing xp'] = "0"
    data['ranged level'] = "1"
    data['ranged xp'] = "0"
    data['thieving level'] = "1"
    data['thieving xp'] = "0"
    data['cooking level'] = "1"
    data['cooking xp'] = "0"
    data['prayer level'] = "1"
    data['prayer xp'] = "0"
    data['crafting level'] = "1"
    data['crafting xp'] = "0"
    data['firemaking level'] = "1"
    data['firemaking xp'] = "0"
    data['magic level'] = "1"
    data['magic xp'] = "0"
    data['fletching level'] = "1"
    data['fletching xp'] = "0"
    data['woodcutting level'] = "1"
    data['woodcutting xp'] = "0"
    data['runecrafting level'] = "1"
    data['runecrafting xp'] = "0"
    data['slayer level'] = "1"
    data['slayer xp'] = "0"
    data['farming level'] = "1"
    data['construction xp'] = "0"
    data['construction level'] = "1"
    data['hunter xp'] = "0"
    data['hunter level'] = "1"
    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()
        main()
def jeps():
    main()
main()
    
