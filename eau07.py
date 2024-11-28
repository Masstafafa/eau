import sys

# Fonctions :

def alternate_case(string):
    alternated_case = ""
    letter_count = 0   # Pour compter uniquement les lettres
    for i in range(len(string)):
        current_char = string[i]
        ascii_value = ord(current_char)

        if ascii_value >= 65 and ascii_value <= 90 or ascii_value >= 97 and ascii_value <= 122:
        
            if letter_count % 2 == 0:   # Pair -> forcer en majuscule
                alternated_case += chr(ascii_value - 32 if ascii_value >= 97 else ascii_value)
            else:                       # Impair -> forcer en minuscule
                alternated_case += chr(ascii_value + 32 if ascii_value <= 90 else ascii_value)
            letter_count += 1
        else:
            alternated_case += current_char
    return alternated_case


# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) != 1:
        print("Erreur : Merci d'indiquer un seul argument entre guillemets")
        return False
    return True

def is_valid_digit(arguments):
    if arguments[0].isdigit():
        print("Erreur : Merci de ne pas indiquer de chiffre")
        return False
    return True

# Récupération de données :

def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution:

def get_alernated_case():
    arguments = get_arguments()
    
    if not is_valid_length(arguments):
        return
    
    if not is_valid_digit(arguments):
        return
    
    result = alternate_case(arguments[0])
    print(result)


#Affichage :

get_alernated_case()