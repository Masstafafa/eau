import sys

# Fonctions :
   
def inverse_arguments(arguments):
    reversed_args = []
    for i in range(len(arguments)-1, -1, -1):  
        reversed_args.append(arguments[i])
    return reversed_args

# Gestion d'erreurs :

def is_valid_arguments(arguments):
    if not arguments:        
        print("Error: Merci d'indiquer au moins un argument")
        return False

# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_reversed_arguments():
    args = get_arguments()
    if not is_valid_arguments(args):
        return
    
    reversed_args = inverse_arguments(args) 
    for arg in reversed_args:
        print(arg)

#Affichage :

display_reversed_arguments()


'''reversed arguments quand arguments inversés
constante varialbes'''