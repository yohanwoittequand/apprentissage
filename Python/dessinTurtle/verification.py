#usr/bin/python3.5
# coding:utf-8

from affichageConsole import *

def saisieDemmarrerJeu():
    return input("Voulez-vous démarrer un partie ? [ O - N ]")


def verifSaisieCommencer(saisieUtilisateur):
    saisieFormater = saisieUtilisateur.strip().lower()
    if saisieFormater[0] == "o":
        return True
    elif saisieFormater[0] == "n":
        affichageFin()
        exit()
    else:
        print("\n\tVotre saisie n'est pas valide.\n\t\tEntrer O ou N\n")
        return False
   

    


        
