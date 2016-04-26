#usr/bin/python3.5
# coding:utf-8

def saisieDemmarrerJeu():
    return input("Voulez-vous démarrer un partie ? [ O - N ]")

def estTypeString(saisieUtilisateur):
    if type(saisieUtilisateur) == type(str()):
        return True

def verifSaisieCommencer(saisieUtilisateur):
    if estTypeString(saisieUtilisateur):
        if saisieUtilisateur[0].lower() == "o":
            return True
    else:
        print("Votre saisie n'est pas valide.\n Entrer O ou N ")
        return False


    


        
