import math
from dict import length_between_city


def menu():
    print("-----------------------------[Menu]-----------------------------")
    print("[1] Voir toute les villes disponible.\n[2] Calculer un temps de trajet.\n[3] Sortir du programme")
    choice = input("Votre choix: ")
    if (choice == 1 or choice == "1"):
        print("\n")
        for city in length_between_city:
            print(city)
        input("\nAppuyez sur entrée pour retourner au menu\n")
        menu()

    elif (choice == 2 or choice == "2"):
        print("Veuillez entrer le nom de la ville avec la première lettre en majuscule.")
        departure = input("Ville de départ: ")
        arrival = input("Ville d'arrivée: ")
        tomtom(departure, arrival)

    elif (choice == 3 or choice == "3"):
        return 1

def tomtom(departure, arrival):
    if(departure != arrival):
        length = length_between_city[departure][arrival] 
        print(length)
        length = length * 1000
        print(length)
        done_length = 0
        seconds = 0
        speed = 0
        last_pause = 0
        pause_count = 0
        have_to_take_pause = False
        while(done_length < length):
            if(seconds != 0 and (seconds - last_pause) % (7200) == 0):
                have_to_take_pause = True
                print(have_to_take_pause)
            if(speed < 90 and have_to_take_pause == False):
                if(speed + 10/60 <= 90):
                    speed += 10/60
                else:
                    speed = 90
            if(have_to_take_pause == True and speed > 0):
                if(speed - 10/60 >= 0):
                    speed -= 10/60
                else:
                    speed = 0
            if(have_to_take_pause == True and speed == 0):
                pause_count += 1
                seconds += 60*15
                last_pause = seconds
                have_to_take_pause = False
            done_length += (speed/3.6)
            seconds += 1
        hours = 0
        minutes = 0
        if(seconds/60 > 0):
            if(seconds/3600 > 0):
                hours = math.floor(seconds/3600)
            minutes = math.ceil((seconds % 3600)/60)
        print(seconds)
        print(pause_count)
        print("-------------------------[Tableau récapitulatif]---------------------------------")
        print("Ville de départ :", departure, "| Ville d'arrivée :", arrival, "|", length/1000, "km | ", "{}:{}".format(hours, minutes), "(avec {} minutes de pause)".format(pause_count * 15))
        print("-------------------------[Tableau récapitulatif]---------------------------------")
        #return 0
        menu()
    else:
        print("\nVous avez entré la même ville pour le départ et l'arrivée.")
        input("\nAppuyez sur entrée pour retourner au menu\n")
        menu()

menu()
