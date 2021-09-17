def pointDeRencontre(v1, v2, distance):
    temps = 0
    # DONE faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    if distance !=0:
        temps = distance/(v1+v2)

    # DONE calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    positionRencontre = v1 * temps

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
