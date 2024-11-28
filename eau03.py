import sys

# Fonctions utilisées:

def fibonacci(index_number):
    fibo_list = [0, 1]
    if index_number == 0:
        return 0
    if index_number == 1:
        return 1
    for i in range(2, index_number + 1):
            new_number = fibo_list[-1] + fibo_list[-2]
            fibo_list.append(new_number)
    return fibo_list[index_number]

# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) != 1:
        print("Erreur(-1) : Merci de n'indiquer qu'un seul chiffre positif")
        return False
    return True

def is_valid_digit(arguments):
    if not arguments[0].isdigit():
        print("Erreur(-1) : Merci d'indiquer un argument qui est un chiffre positif")
        return False
    return True
      

# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def calculate_fibonacci():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    if not is_valid_digit(arguments):
        return
 
    answer = fibonacci(int(arguments[0]))
    print(answer)

# Affichage :

calculate_fibonacci()