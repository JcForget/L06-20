import math


def resoudreEquation(a, b, c):

    #Définition variables
    naPasDeSolution=aUneSeuleSolution=aDeuxSolutions=False


    # DONE: Calculer le discriminant et assigner la valeur dans la variable "delta"
    delta = (b**2)-4*a*c

    # DONE: Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
    if delta<0:
        naPasDeSolution = True


    if naPasDeSolution:
        # ces lignes de code seront executés s'il n'y aucune racine
        # DONE: afficher sur l'écran "Aucune racine"
        print('\n Aucune solution réelle \n')
        # ne pas modifier
        return None

    # DONE: Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    if delta==0:
        aUneSeuleSolution = True

    if aUneSeuleSolution:
        # ces lignes de code seront executés s'il n'y a qu'une seule racine
        # DONE: afficher sur l'écran "Une seule racine"
        print('\n Une seule racine \n')
        # DONE: assigner a la variable x1 la valeur de la racine
        x1 = -b/(2*a)
        # ne pas modifier
        return x1

    # DONE: Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
    if delta>0:
        aDeuxSolutions = True

    if aDeuxSolutions:
        # DONE: afficher sur l'écran "Deux racines"
        print('\n Deux racines \n')
        # DONE: calculer la prmiere racine, assigner la a "x1"
        x1 =(-b+delta**(0.5))/(2*a)

        # DONE: calculer la deuxieme racine, assigner la a "x2"
        x2 = (-b-delta**(0.5))/(2*a)

        # ne pas modifier cette ligne
        return x1, x2


if __name__ == '__main__':
    a = int(input("Entrez a, non nul: "))
    b = int(input("Entrez b: "))
    c = int(input("Entrez c: "))

    print(resoudreEquation(a, b, c))
