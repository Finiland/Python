import random
import os
import time
import json
import math


print("Tervetuloa pelaamaan kivipaperisakset-peliä. Vaihtoehtoina ovat kaksinpeli ja yksinpeli.")
print("Paina ENTER-näppäintä, kun haluat mennä eteenpäin.\n")
odotusInput = input()
os.system("clear")
if os.path.isdir("scoreforgame") == False:
        os.mkdir("scoreforgame")
        os.chdir("scoreforgame/")
        os.mknod("score.json")
        with open("score.json", "w") as f:
            f.write("{}")
            f.close()
elif os.path.isfile("scoreforgame/score.json") == True:
    pass
PerusVari = '\033[0m'
global pelinArvo
global pelinArvoNimi
global PeliMaara
global Haviot
global Tasapelit
global Voitot
global PeliTunnistus
def pelinValitsin():
    peliMuotoValitsin = input("Haluatko pelata yksin tietokonetta vastaan vai kaverin kanssa? Jos haluat yksin, laita 1. Jos kaksin, laita 2. \n Numero 3:lla näet statsit. Numero 4:lla voit nollata statsisi. \n")
    if peliMuotoValitsin == "1":
        yksinpeli()
    elif peliMuotoValitsin == "2":
        kaksinpeli()
    elif peliMuotoValitsin == "3":
        PelinStatsit("Tarkistus", "Tarkistus")
    elif peliMuotoValitsin == "4":
        PelinStatsit("Puhdistus", "Puhdistus")
    # Tämä "debug" on vain Debuggaukseen käytetty
    #elif peliMuotoValitsin == "debug":
        #PelinStatsit("Testi", 3)
        #print(math.ceil(8/(27-11)*100))
    else:
        print("Nyt oli väärä input, ota uudelleen")
        time.sleep(1)
        os.system("clear")
        pelinValitsin()
        

def uusiPeli(pelinArvo):
    pelinArvo = pelinArvo
    os.system("clear")
    uusiPeliInput = input("Haluatko ottaa uuden pelin? Y/N\n")
    if pelinArvo == 1 and uusiPeliInput in ("Y", "y", "yes", '\033[0m'"Yes"):
        yksinpeli()
    elif pelinArvo == 2 and uusiPeliInput in ("Y", "y", "yes", "Yes"):
        kaksinpeli()
    elif uusiPeliInput in ("N", "n", "No", "no"):
        print("Kiitos peleistä! Nähdään ensi kerralla!")
    else:
        uusiPeli(pelinArvo)

def PelinStatsit(pelinArvoNimi, PeliTunnistus):
    #PeliTunnistus 1 = Tasapeli
    #PeliTunnistus 2 = Häviö
    #PeliTunnistus 3 = Voitto

    if os.path.isfile("score.json") == False:
        os.chdir("scoreforgame/")
        PelinStatsit(pelinArvoNimi, PeliTunnistus)
    else:
        with open("score.json", "r") as f:
            data = json.load(f)
            f.close()
        if not f'{pelinArvoNimi}' in data and f'{pelinArvoNimi}' != "Puhdistus" and f'{PeliTunnistus}' != "Puhdistus" and f'{pelinArvoNimi}' != "Tarkistus" and f'{PeliTunnistus}' != "Tarkistus":
            data[f'{pelinArvoNimi}'] = {}
            data[f'{pelinArvoNimi}']['Pelimaara'] = 0
            data[f'{pelinArvoNimi}']['Voitot'] = 0
            data[f'{pelinArvoNimi}']['Haviot'] = 0
            data[f'{pelinArvoNimi}']['Tasapelit'] = 0
            data[f'{pelinArvoNimi}']['Voittoprosentti'] = 0

        elif f'{pelinArvoNimi}' == "Puhdistus" and f'{PeliTunnistus}' == "Puhdistus":
            Varmistus = input("Oletko varma, että haluat nollata tilastosi? Kirjoita " '\33[93m' + 'Kyllä ' + PerusVari + "ilman heittomerkkejä (huomioi isot kirjaimet). Tässä kestää hetken.\n")
            if Varmistus == "Kyllä":
                time.sleep(3)
                os.system("clear")
                time.sleep(1)
                print("XOOOOOOOOO")
                time.sleep(1)
                print("XXOOOOOOOO")
                time.sleep(1)
                print("XXXOOOOOOO")
                time.sleep(1)
                print("XXXXOOOOOO")
                time.sleep(1)
                print("XXXXXOOOOO")
                time.sleep(1)
                print("XXXXXXOOOO")
                time.sleep(1)
                print("XXXXXXXOOO")
                time.sleep(1)
                print("XXXXXXXXOO")
                time.sleep(1)
                print("XXXXXXXXXO")
                time.sleep(1)
                print("XXXXXXXXXX")
                time.sleep(2)
                print('\33[93m' + "Tilastosi on nollattu!" + PerusVari)
                time.sleep(5)
                os.system("clear")
                data["Yksinpeli"]['Pelimaara'] = 0
                data["Yksinpeli"]['Voitot'] = 0
                data["Yksinpeli"]['Haviot'] = 0
                data["Yksinpeli"]['Tasapelit'] = 0
                data["Yksinpeli"]['Voittoprosentti'] = 0
                with open("score.json", "w", encoding="utf-8") as f:
                    data = json.dump(data, f, indent=4)
                    f.close()
                print("Pelimäärä:", "\33[33m", data["Yksinpeli"]['Pelimaara'], '\033[0m' "\n")
                print("Voitot:", "\33[33m", data["Yksinpeli"]['Voitot'], '\033[0m'"\n")
                print("Häviöt:", "\33[33m", data["Yksinpeli"]['Haviot'], '\033[0m'"\n")
                print("Tasapelit:", "\33[33m", data["Yksinpeli"]['Tasapelit'], '\033[0m'"\n")
                print("Voittoprosentti:", "\33[33m", data["Yksinpeli"]['Voittoprosentti'], '\033[0m'"\n")
                time.sleep(5)
                os.system("clear")
                pelinValitsin()
            else:
                print("\33[33m", "Kirjoitit väärin." + PerusVari)
                input("ENTER-näppäimellä eteenpäin!")
                os.system("clear")
                pelinValitsin()
        elif f'{pelinArvoNimi}' == "Tarkistus" and f'{PeliTunnistus}' == "Tarkistus":
            os.system("clear")
            print("Pelimäärä:", "\33[33m", data["Yksinpeli"]['Pelimaara'], '\033[0m' "\n")
            print("Voitot:", "\33[33m", data["Yksinpeli"]['Voitot'], '\033[0m'"\n")
            print("Häviöt:", "\33[33m", data["Yksinpeli"]['Haviot'], '\033[0m'"\n")
            print("Tasapelit:", "\33[33m", data["Yksinpeli"]['Tasapelit'], '\033[0m'"\n")
            print("Voittoprosentti:", "\33[33m", data["Yksinpeli"]['Voittoprosentti'], '\033[0m'"\n")
            input('\33[31m' + "ENTER-näppäimellä pääsee takaisin main menuun!" + '\033[0m')
            os.system("clear")
            pelinValitsin()



        elif PeliTunnistus == 1:
            data[f'{pelinArvoNimi}']['Pelimaara'] += 1
            data[f'{pelinArvoNimi}']['Tasapelit'] += 1
        
        elif PeliTunnistus == 2:
            data[f'{pelinArvoNimi}']['Pelimaara'] += 1
            data[f'{pelinArvoNimi}']['Haviot'] += 1
            data[f'{pelinArvoNimi}']['Voittoprosentti'] = math.ceil(data[f'{pelinArvoNimi}']['Voitot'] / data[f'{pelinArvoNimi}']['Pelimaara'] * 100)
        
        elif PeliTunnistus == 3:
            data[f'{pelinArvoNimi}']['Pelimaara'] += 1
            data[f'{pelinArvoNimi}']['Voitot'] += 1
            data[f'{pelinArvoNimi}']['Voittoprosentti'] = math.ceil(data[f'{pelinArvoNimi}']['Voitot'] / data[f'{pelinArvoNimi}']['Pelimaara'] * 100)
        with open("score.json", "w", encoding="utf-8") as f:
            data = json.dump(data, f, indent=4)
            f.close()

def yksinpeli():
    pelinArvo = 1
    pelinArvoNimi = "Yksinpeli"
    if os.path.isfile("score.json") == False:
        os.chdir("scoreforgame/")
    os.system("clear")
    AiValintaLista = ["sakset", "paperi", "kivi"]
    AiValinta = random.choice(AiValintaLista)
    print(AiValinta, "##################################")
    pelaajanValinta = input("Minkä haluat valita? Kivi, paperi vai sakset?\n")
    if pelaajanValinta in ("Kivi", "kivi", "Paperi", "paperi", "Sakset", "sakset"):
        if pelaajanValinta in ("Kivi", "kivi") and AiValinta == "kivi":
            PeliTunnistus = 1
            print(PeliTunnistus)
            print("Tasapeli!")
            input("ENTER-näppäimellä eteenpäin!")            
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo)
            
            
        elif pelaajanValinta in ("Kivi", "kivi") and AiValinta == "paperi":
            print("Hävisit!")
            input("ENTER-näppäimellä eteenpäin!")
            PeliTunnistus = 2
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo)
            
        elif pelaajanValinta in ("Kivi", "kivi") and AiValinta == "sakset":
            print("Voitit!")
            input("ENTER-näppäimellä eteenpäin!")
            PeliTunnistus = 3
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo)
            
        elif pelaajanValinta in ("Paperi", "paperi") and AiValinta == "paperi":
            print("Tasapeli!")
            input("ENTER-näppäimellä eteenpäin!")
            PeliTunnistus = 1
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo)
            
        elif pelaajanValinta in ("Paperi", "paperi") and AiValinta == "sakset":
            print("Hävisit!")
            input("ENTER-näppäimellä eteenpäin!")
            PeliTunnistus = 2
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo)  

        elif pelaajanValinta in ("Paperi", "paperi") and AiValinta == "kivi":
            print("Voitit!")
            input("ENTER-näppäimellä eteenpäin!")
            PeliTunnistus = 3
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo)    

        elif pelaajanValinta in ("Sakset", "sakset") and AiValinta == "sakset":
            print("Tasapeli!")
            input("ENTER-näppäimellä eteenpäin!")
            PeliTunnistus = 1
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo) 

        elif pelaajanValinta in ("Sakset", "sakset") and AiValinta == "kivi":
            print("Hävisit!")
            input("ENTER-näppäimellä eteenpäin!")
            PeliTunnistus = 2
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo)
            
        elif pelaajanValinta in ("Sakset", "sakset") and AiValinta == "paperi":
            print("Voitit!")     
            input("ENTER-näppäimellä eteenpäin!")
            PeliTunnistus = 3
            PelinStatsit(pelinArvoNimi, PeliTunnistus)
            uusiPeli(pelinArvo)
            
        else:
            yksinpeli()
    else:
        print("Nyt oli kyllä väärä input. Kokeile uudestaan.")
        time.sleep(1)
        yksinpeli()







def kaksinpeli():
    pelinArvo = 2
    pelinArvoNimi = "Kaksinpeli"
    os.system("clear")



pelinValitsin()