from models.joueur import Player
from functions.jeux import *
from datetime import datetime

def main():
    print("\n_________________________________________________")
    print('\nBienvenue sur le jeu VIDEO POKER BY LOUIS')
    print("\n_________________________________________________")
    annee_actuelle = 2022
    annee_naissance = int(input("rentrez votre année de naissance : "))
    age = annee_actuelle - annee_naissance
    print (age)
    if age >= 18:
        pass
    else : 
        print("vous n'avez pas l'age requis")
        exit()
    print("\n_________________________________________________")
    name = input("\nQuel est votre nom ? ")
    print("\n_________________________________________________")
    money = int(input("\nBonjour " + name + ". Combien de crédit voulez-vous acheter ? "))
    print("\n_________________________________________________")
    print("\nTrès bien, commençons la partie. Bonne Chance " + name + "!!")
    print("\n_________________________________________________")
    

    player = Player(name, money, [])

    while player.get_money() > 0:
        bet_value = int(input("\nCombien Voulez-vous miser ? "))
        print("\n_________________________________________________")
        if bet_value <= player.get_money():
            jeux(bet_value, player)
        else:
            print("\nJe suis désolé mais vous n'avez pas assez de crédit ")
            print("\n_________________________________________________")

    if player.get_money() < 1:
        print("\nJe suis désolé mais vous avez perdu tout vos crédits.\nVous aurez plus de chance la prochaine fois.")
        print("\n_________________________________________________")
        still_playing = input("\nVoulez-vous recommencer la partie ? oui/non ")
        if still_playing == "oui":
            main()
        else:
            print("\n_________________________________________________")
            print("Au revoir " + player.get_name())


main()