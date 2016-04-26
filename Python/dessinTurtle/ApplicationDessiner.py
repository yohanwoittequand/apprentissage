#/usr/bin/python3.5
# coding:utf-8

from verification import *
from affichageConsole import *

affichageDebut()

veutJouer= saisieDemmarrerJeu()

while verifSaisieCommencer(veutJouer) == False:
    veutJouer= saisieDemmarrerJeu()
    verifSaisieCommencer(veutJouer)

print()
print("On peut commencer")
#retour = verifSaisieCommencer(veutJouer)

#Faire un fonction de vérification en fonction des erreurs possible pour renvoyer un boolean




affichageFin()
