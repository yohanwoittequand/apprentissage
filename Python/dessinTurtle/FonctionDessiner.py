#/usr/bin/python3.5
# coding:utf-8

from turtle import *



def dessineCarre(couleur, taille):
    """
        Dessine un carre

        couleur : designe la couleur des bordures du carré
        taille : détermine la longueur d'un coté du carré
    """
    for cote in range(0,4):
        color(couleur)
        forward(taille)
        left(90)
   

def dessineTriangle(couleur, taille):
    """
        Dessine un Triangle

        couleur : designe la couleur des bordures du carré
        taille : détermine la longueur d'un coté du carré
    """
    for cote in range(0,3):
        color(couleur)
        forward(taille)
        left(120)


def dessineHexagone(couleur, taille):
    """
        Dessine un Hexagone

        couleur : designe la couleur des bordures du carré
        taille : détermine la longueur d'un coté du carré
    """
    for cote in range(0,6):
        color(couleur)
        forward(taille)
        left(60)




    
