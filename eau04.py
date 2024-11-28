import sys
# Fonctions utilisées:
# verifier que n+1 n'est pas premier si il ne l'est pas ajouter 1 puis verifier de nouveau si 
# il est premier, arreter la fonction et retourner le chiffre en question 

def next_prime_number(arguments):
    number = int(arguments[0])
    test_number = number + 1
    while True:
        is_prime = True
        for i in range(2, test_number):
            if test_number % i == 0:
                is_prime = False
                break
        if is_prime:
            return test_number
        test_number += 1

# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) != 1:
        print("Erreur : Merci d'indiquer un seul argument qui est un nombre premier")
        return False
    return True

def is_valid_digit(arguments):
    if not arguments[0].isdigit():
        print("Erreur : Merci d'indiquer un chiffre")
        return False
    return True

def is_number_zero_or_one(arguments):
    if arguments[0] == "0" or arguments[0] == "1":
        print("2")
        return False
    return True

# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def get_next_prime_number():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    if not is_valid_digit(arguments):
        return
    if not is_number_zero_or_one(arguments):
        return
    prime_number = next_prime_number(arguments)
    print(prime_number)

# Affichage :

get_next_prime_number()