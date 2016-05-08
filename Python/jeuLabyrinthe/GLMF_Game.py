#usr/bin python

import JeuMain

if __name__ == "__main__":
    perso ="X"
    pos_perso = [1,1]
    n_levels_total = 20

    for n_level in range(1, n_levels_total + 1):
        level = JeuMain.charge_labyrinthe("level_" + str(n_level))
        JeuMain.jeu(level, n_level, perso, pos_perso)
    print("vous avez gagné la partie") 
