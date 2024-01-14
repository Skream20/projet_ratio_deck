import random

print("   Programme Atem : V.0.0   ")
print("  Starting Hand Calculator")
print(" ****************************\n")

CarteVoulue = input(
    "Quelle carte souhaitez-vous tirer (Veuillez entrer le nom exact) ? >>> "
)
nbTirages = int(input("Combien de tirages voulez-vous effectuer ? >>> "))
nbDeFoisTiree = 0


decklist = [
    "Wulf",
    "Wulf",
    "Wulf",
    "Raiden",
    "Raiden",
    "Raiden",
    "Lumina",
    "Ryko",
    "Charge",
    "Charge",
    "Charge",
    "Chaos Emperor Dragon",
    "Levianeer",
    "Levianeer",
    "Levianeer",
    "Creator",
    "Nephthys",
    "Valkyria",
    "Valkyria",
    "Valkyria",
    "Collapserpent",
    "Wyverbuster",
    "Seyfert",
    "Chaos Space",
    "Chaos Space",
    "Chaos Space",
    "Eldlich",
    "Nessie",
    "Nessie",
    "Mothman",
    "Chupacabra",
    "Jackalope",
    "Snek",
    "Photon Thrasher",
    "Trick Clown",
    "Plague",
    "Reinforcements of the Army",
    "Foolish",
    "Monster Reborn",
    "Order",
]

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

    decklist = decklist + [
        "Wulf",
        "Wulf",
        "Wulf",
        "Raiden",
        "Raiden",
        "Raiden",
        "Lumina",
        "Ryko",
        "Charge",
        "Charge",
        "Charge",
        "Chaos Emperor Dragon",
        "Levianeer",
        "Levianeer",
        "Levianeer",
        "Creator",
        "Nephthys",
        "Valkyria",
        "Valkyria",
        "Valkyria",
        "Collapserpent",
        "Wyverbuster",
        "Seyfert",
        "Chaos Space",
        "Chaos Space",
        "Chaos Space",
        "Eldlich",
        "Nessie",
        "Nessie",
        "Mothman",
        "Chupacabra",
        "Jackalope",
        "Snek",
        "Photon Thrasher",
        "Trick Clown",
        "Plague",
        "Reinforcements of the Army",
        "Foolish",
        "Monster Reborn",
        "Order",
    ]

print(CarteVoulue + " a été tirée " + str(nbDeFoisTiree) + " fois")



