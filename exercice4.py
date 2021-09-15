import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # DONE faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    positionInitiale /= 1000
    duree /= 3600
    acceleration  = (vitesseFinale - vitesseInitiale)/duree

    # DONE calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = (vitesseInitiale*duree + 0.5*acceleration*duree**2)*1000

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
