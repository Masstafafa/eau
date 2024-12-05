import sys

# Fonctions utilisées:

def is_number(arguments):
    argument = arguments[0]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in argument:
        if i not in numbers:
            return False
    return True

# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) != 1:
        print("Erreur : Merci d'indiquer un seul argument")
        return False
    return True

# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def resolve():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    is_number(arguments)
    result = is_number(arguments)
    if result:
        print("true")
    else:
        print("false")
    
# Affichage :

resolve()