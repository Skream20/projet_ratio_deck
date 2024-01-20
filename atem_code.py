import random

print("   Programme Atem : V.0.0   ")
print("  Starting Hand Calculator")
print(" ****************************\n")

CarteVoulue = input(
    "Quelle carte souhaitez-vous tirer (Veuillez entrer le nom exact) ? >>> "
)
nbTirages = int(input("Combien de tirages voulez-vous effectuer ? >>> "))
nbDeFoisTiree = 0

tirage = []


for i in range(nbTirages):
    for i in range(5):
        random.shuffle(decklist)

        if decklist[0] == CarteVoulue and decklist[0] not in tirage:
            nbDeFoisTiree = nbDeFoisTiree + 1
            tirage.append(print(decklist.pop()))
        else:
            tirage.append(print(decklist.pop()))

    print("----------------------------\n")

    decklist.clear()
    tirage.clear


print(CarteVoulue + " a été tirée " + str(nbDeFoisTiree) + " fois")



