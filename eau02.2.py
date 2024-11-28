import sys

# Récupérer les arguments rentrer par l'utilisateur puis les inverser
'''arguments = sys.argv[1:]
reversed_arguments = arguments[::-1]

if not arguments:
    print("Error: Merci de rentrer au moins un argument")
    sys.exit()

for words in reversed_arguments:
    print(words)'''


'''arguments = sys.argv[1:]

if not arguments:
    print("Error: Merci de rentrer au moins un argument")
    sys.exit()

#arguments.reverse()


reversed_arguments = list(reversed(arguments))
print(reversed_arguments)

for words in reversed_arguments:
    print(words)'''
import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    print("erreur.")
    sys.exit()

dividend = int(arguments[0])
divisor = int(arguments[1])

if divisor == 0:
    print("erreur.")
    sys.exit()
if dividend < divisor:
    print("erreur.")
    sys.exit()

rest = (dividend % divisor)
result = (dividend / divisor)

print(f"résultat: {int(result)}")
print(f"reste: {rest}")