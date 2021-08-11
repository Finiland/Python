import random
import math
import time
import json
import woodcutting as WC




def main():
    inputteriino = input('Mitä haluat tehdä?: ')
    if inputteriino == ("start game"):
        start_game()
    if inputteriino == ("chop"):
        WC.cutChoiceLogs()
        
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
    data['woodcutting level'] = "1"
    data['woodcutting xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    data['attack level'] = "1"
    data['attack xp'] = "0"
    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()
        main()
    


main()