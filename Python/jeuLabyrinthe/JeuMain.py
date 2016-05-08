# usr/bin/ python
# coding:utf-8
lab = (
	"+---------+",
	"+         +",
	"+         +",
	"+         +",
	"+         +",
	"+        O+",
	"+---------+"
        )


def affichage_labyrinthe(labyrinthe,perso,position_perso):
    """
    labyrinthe a creer en dehors
    perso = "X"
    position_perso = [colonne,ligne]
    """
    n_ligne = 0
    for ligne in labyrinthe:
        if n_ligne == position_perso[1]:
            print(ligne[0:position_perso[0]]+perso+ligne[position_perso[0]+1:])
        else:
            print(ligne)
        n_ligne = n_ligne + 1 
            
def verification_deplacement(lab,pos_col, pos_ligne):
    """
    Indique si le déplacement du personnage est autorisé ou pas.

    lab : labyrinthe
    position_colonne : position du personnage sur les colonnes
    position_ligne : position du personage sur les lignes

    Valeur de retour :
        None : déplacement interdit
        [col , ligne] : déplacement autorisé sur la case indiquée par la liste
    """
    # Calcul de la taille du labyrinthe
    n_cols = len(lab[0])
    n_lignes = len(lab)

    # Test si le déplacement conduit le pesonnage en dehors de l'aire de jeu

    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or \
       pos_col > (n_cols - 1):
        return None
    elif lab[pos_ligne][pos_col] !=" ":
        return None
    elif lab[pos_ligne][pos_col] == "O":
        return [-1, -1]
    else:
        return [pos_col, pos_ligne] # renvoie des coordonnées valides pour perso

    
def choix_joueur(lab, pos_perso):
    """
    Demande au joueur de saisir son déplacement et vérifie si il est possible.
    Si ce n'est pas le cas affiche un message, sinon modifie la position du
    perso dans la liste pos_perso

    lab : labyrinthe
    pos_perso : liste contenant la position du personnage [colonne, ligne}

    Pas de valeur de retour
    """

    choix = input("Votre déplacement (Haut/Bas/Gauche/Droit/Quitter) ? ")
    if choix == "h" :
        dep = verification_deplacement(lab, pos_perso[0], pos_perso[1] - 1)
        print(dep)
    elif choix == "b":
        dep = verification_deplacement(lab, pos_perso[0], pos_perso[1] + 1)
        print(dep)
    elif choix == "g":

        dep = verification_deplacement(lab, pos_perso[0] - 1, pos_perso[1])
        print(dep)
    elif choix == "d":
        dep = verification_deplacement(lab, pos_perso[0] + 1, pos_perso[1])
        print(dep)
    elif choix == "q":
        exit(0)

    if dep == None:
        print("Déplacement impossible")
    else:
        pos_perso[0] = dep[0]
        pos_perso[1] = dep[1]

    
def jeu(level, perso, pos_perso):
    while True:
        affichage_labyrinthe(level,perso, pos_perso)
        choix_joueur(level, pos_perso)
        if pos_perso == [-1, -1]:
            print("Vous avez passé le niveau")
            break
        

perso ="X"
pos_perso = [1,1]
jeu(lab,perso,pos_perso)

