import sys

# Fonctions utilisées:

def get_values(arguments):
    arguments.sort()
    number_min = int(arguments[0])
    number_max = int(arguments[1])
    
    for i in range(number_min, number_max):
        print(i, end=" ")


# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) != 2:
        print("Erreur : Merci d'indiquer deux arguments qui sont des chiffres")
        return False
    return True


def is_valid_arguments(arguments):
    if not arguments[0].isdigit() or not arguments[1].isdigit():
        print("Erreur : Merci d'indiquer des chiffres")
        return False
    return True

# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_numbers():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    if not is_valid_arguments(arguments):
        return
    get_values(arguments)
    

# Affichage :

display_numbers()