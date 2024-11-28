import sys

# Fonctions utilisées:

def find_diff_min(arguments):
    numbers = list(map(int, arguments))
    numbers.sort()
    diff_min = float("inf")
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]     
        if diff < diff_min:
            diff_min = diff
    return diff_min
       
        
# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) < 2:
        print("Erreur : Merci d'indiquer au moins deux arguments")
        return False
    return True

def is_valid_arguments(arguments):
    for argument in arguments:
        if not argument.lstrip('-').isdigit():
            print("Erreur : Merci d'indiquer au moins deux arguments qui sont des nombres positifs négatifs")
            return False
    return True
    
# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments  

# Résolution :

def display():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    if not is_valid_arguments(arguments):
        return
    print(find_diff_min(arguments))
    

# Affichage :

display()