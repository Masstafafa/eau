import sys

# Fonctions utilisées:



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

def display():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    answer = arguments[0]
    print(f"J’ai terminé l’Épreuve de l’Eau et c’était {answer}")

# Affichage :

display()