import sys

# Fonctions utilisées:

def my_select_sort(array):
    array = list(map(int, array))
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
                array[i], array[min] = array[min], array[i]        
    return " ".join(map(str, array))
    
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
    print(my_select_sort(arguments))

# Affichage :

display()