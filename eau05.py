import sys

# Fonctions :

def is_repeat_arguments(first_argument, second_argument):
    for i in range(len(first_argument) - len(second_argument) + 1):
        if first_argument[i:i+len(second_argument)] == second_argument:
            print("true")
            return
    print("false")
   
# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) != 2:
        print("Erreur : Merci d'indiquer exactement deux arguments")
        return False
    return True

# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution:

def print_answer():
    arguments = get_arguments()
    first_argument = arguments[0]
    second_argument = arguments[1]
    if not is_valid_length(arguments):
        return
    is_repeat_arguments(first_argument, second_argument)

#Affichage :

print_answer()