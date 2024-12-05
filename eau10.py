import sys

# Fonctions utilisées:

def find_index(arguments):
    last_argument = arguments[-1]
    all_other_arguments = arguments[:-1]
    
    for i in range(len(all_other_arguments)):
        current_argument = all_other_arguments[i]
        if current_argument == last_argument:
            return i
    else:
        return -1
        
# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) < 2:
        print("Erreur : Merci d'indiquer au moins deux arguments")
        return False
    return True

# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments  

# Résolution :

def print_index():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    print(find_index(arguments))

# Affichage :

print_index()