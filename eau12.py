import sys

# Fonctions utilisées:

def my_bubble_sort(array):
    array = list(map(int, array))
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return" ".join(map(str, array))
    

# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) < 2:
        print("Erreur : Merci d'indiquer au moins deux arguments")
        return False
    return True

def is_valid_arguments(arguments):
    for argument in arguments:
        if not argument.isdigit():
            print("Erreur : Merci d'indiquer au moins deux arguments qui sont des nombres positifs")
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
    print(my_bubble_sort(arguments))

# Affichage :

display()