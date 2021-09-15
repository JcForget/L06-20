def fizzBuzz(n):
    # Voici les constantes que nous utiliserons pour le programme.
    multiple_trois = ''
    multiple_cinq  = ''
    # La variable résultat est convertie en string pour pouvoir l'additionner à la fin
    resultat = str(n)

    # DONE imprimer la chaine de caractère appropriée avec la fonction print().
    #Retourne TRUE si c'est un multiple de 3, sinon FALSE
    if n%3==0:
        multiple_trois = 'fizz'
        resultat = ''
    if n%5==0:
        multiple_cinq  = 'buzz'
        resultat = ''

    # Done Assigner ensuite la valeur à la variable resultat
    # Ici, les valeurs sont additionnées pour pouvoir ensuite les écrire avec return
    resultat = resultat + multiple_trois + multiple_cinq
    return resultat

# Cette loupe ne sert qu'à demander le nombre au début du programme puis imprimer le résultat!
if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
