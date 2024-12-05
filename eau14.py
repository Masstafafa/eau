import sys

# Fonctions utilisées:

def ascii_sort(arguments):
    for i in range(len(arguments)):
        min = i
        for j in range(i+1, len(arguments)):
            if arguments[j] < arguments[min]:
                min = j
        arguments[i], arguments[min] = arguments[min], arguments[i]        
    return " ".join(arguments)

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

def display():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    print(ascii_sort(arguments))

# Affichage :

display()