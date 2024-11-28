import sys

# Fonctions :

def capitalize_words(string):
    capitalize_string = ""
    for i in range(len(string)):
        current_char = string[i]
        ascii_value = ord(current_char)
        
        if ascii_value >= 65 and ascii_value <= 90 or ascii_value >= 97 and ascii_value <= 122:
            
            if i == 0 or string[i-1].isspace():
            
                if ascii_value >= 97: 
                    capitalize_string += chr(ascii_value - 32)
                else: 
                    capitalize_string += current_char
            else:
                
                if ascii_value <= 90:  
                    capitalize_string += chr(ascii_value + 32)
                else:  
                    capitalize_string += current_char
        else:
            capitalize_string += current_char
    return capitalize_string


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

def get_string_capitalize():
    arguments = get_arguments()
    
    if not is_valid_length(arguments):
        return
    
    if not is_valid_digit(arguments):
        return
    
    result = capitalize_words(arguments[0])
    print(result)


#Affichage :

get_string_capitalize()