def fizzBuzz(n):
    # Voici les constantes que nous utiliserons pour le programme.
    resultat = ''

    # DONE imprimer la chaine de caractère appropriée avec la fonction print().
    if n % 3==0:
        resultat += 'fizz'
    if n % 5==0:
        resultat += 'buzz'
    if resultat=='':
        resultat = n

    # Done Assigner ensuite la valeur à la variable resultat
    return resultat

# Cette loupe ne sert qu'à demander le nombre au début du programme puis imprimer le résultat!
if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
