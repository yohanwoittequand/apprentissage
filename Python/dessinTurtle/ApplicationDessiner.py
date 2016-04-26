#/usr/bin/python3.5
# coding:utf-8

from verification import *

print("{0}{1}Dessiner c'est gagner{1}{0}".format("#"*8,"-"*3))

print()

commencePartie= saisieDemmarrerJeu()

retour = verifSaisieCommencer(commencePartie)

#Faire un fonction de vérification en fonction des erreurs possible pour renvoyer un boolean

print(retour)



print("{0}{1}Fin du jeu ... A bientôt {1}{0}".format("#"*8,"-"*3))
