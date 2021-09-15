
def decomposer(secondes):
    # Variables pour remplacer les chiffres
    # 60 (min)*60(heure)*24(jour)*365(année)
    uneAnnée = 60*60*24*365
    # 60 (min)*60 (heure)*24 (jour)* 7 (semaine)
    septJours = 60*60*24*7
    # 60 (min)*60 (heure)*24 (jour)
    unJour = 60*60*24
    # 60 (min)*60 (heure)
    uneHeure = 60*60
    # 60 (min)
    uneMinute = 60


    # DONE: Assigner à la variable "annees" le nombre d'années

    annees = secondes//uneAnnée
    reste  = secondes % uneAnnée
    # DONE: Assigner à la variable "semaines" le nombre de semaines restantes
    if reste != 0:
        semaines = reste//septJours
        reste =reste % septJours

    # DONE: Assigner à la variable "jours" le nombre de jours restants
    if reste != 0:
        jours = reste//unJour
        reste =reste % unJour

    # DONE: Assigner à la variable "heures" le nombre d'heures restantes
    if reste != 0:
        heures = reste // uneHeure
        reste = reste % uneHeure

    # DONE: Assigner à la variable "minute" le nombre de minutes restantes
    if reste != 0:
        minutes = reste // uneMinute
        reste = reste % uneMinute

    # DONE: Assigner à la variable "secondes" le nombre de secondes restantes
    if reste != 0:
        secondes = reste


    # DONE: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
