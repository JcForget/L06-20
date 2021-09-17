import matplotlib.pyplot as plt
import math
import numpy as np


def trouverAngle(nombreComplexe):
    return np.angle(nombreComplexe, deg=True)

def trouverModule(nombreComplexe):
    # On peut décomposer le nombre complexe grace au fonction real() et imag()
    # TODO: Calculer le module du nombre complexe et l'assigner dans "module"
    module = (np.real(nombreComplexe)**2 + np.imag(nombreComplexe)**2)**0.5


    return module



def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

    module = trouverModule(nombreComplexe)
    angle = trouverAngle(nombreComplexe)

    # DONE: Afficher le module et l'angle du nombre complexe (3 decimales de précision)
    # La fonction round(nombre,décimale) permet d'arrondir à 3 décimales prêt
    phrase = "\n Le nombre complexe avait un module de {module:.3f} et un angle de {angle:.3f}\n"
    print(phrase.format(module=module,angle=angle))

    # DONE: Calculer le nouveau nombre complexe après rotation, assigner le nouveau nombre complexe à la variable 'resultat'
    # Multiplication de l'ancien nombre complexe par cos(angle)+sin(angle)i
    nombreComplexe *= complex(math.cos(angle_rotation),math.sin(angle_rotation))
    resultat = nombreComplexe

    nouveauModule = trouverModule(resultat)
    nouvelAngle = trouverAngle(resultat)

    # TODO : Afficher le nouveau module et le nouvel angle du nombre complexe après rotation (3 decimales de précision)
    phrase = "\n Le nombre complexe a maintenant un module de {module:.3f} et un angle de {angle:.3f}\n"
    print(phrase.format(module=nouveauModule, angle=nouvelAngle))
    return resultat


def dessiner(number, label):
    ax = plt.subplot(projection='polar')
    if number != None:
        ax.plot([0, math.radians(trouverAngle(number))], [0, trouverModule(number)], marker='o', label=label)

if __name__ == '__main__':
    nombre = complex(input("Veuillez entrer un nombre complexe de votre choix sous la forme a+bj (exemple: 1+2j): "))
    rotation = float(input("Veuillez entrer un angle de rotation (en degres) de votre choix (exemple: 87): "))

    try:
        resultat = effectuerRotation(nombre, rotation, trouverModule)
    except Exception as e:
        print(e)
        resultat = None

    dessiner(nombre, 'Avant rotation')
    dessiner(resultat, 'Après rotation')
    plt.legend()
    plt.show()
