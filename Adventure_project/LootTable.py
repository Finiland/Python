import random
import math
import json
import time
import os


def addItemToBank(item, quantity):
    with open('bank.json', 'r') as f:
        data = json.load(f)
        f.close()
    if not item in data:
        data[f'{item}'] = {}
        data[f'{item}']['name'] = item
        data[f'{item}']['quantity'] = quantity
    
    else:
        data[f'{item}']['quantity'] += quantity
    with open('bank.json', 'w') as f:
        data = json.dump(data, f, indent=4)
        f.close()
'''
def statusCheck():
    with open('status.txt', 'r') as f:
        data = json.load(f)
        f.close()
    if data == 1:
        print("Banked the logs into your bank. Currently you have: ")'''

def checkItemFromBank(item, quantity):
    with open('bank.json', 'r') as f:
        data = json.load(f)
    
    name = data[f'{item}']['name'] 
    quantity = data[f'{item}']['quantity']
    return name, quantity
    
def minusItemFromBank(item, quantity):
    with open('bank.json', 'r') as f:
        data = json.load(f)
    minus = data[f'{item}']['quantity'] - quantity
    