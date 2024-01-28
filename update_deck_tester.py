import json
import requests
import random


def get_card_name(card_id):
    for card in db:
        if card["id"] == card_id:
            return card["name"]
    return "Carte non trouvée"

def load_ygo_db():

    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    response = requests.get(base_url)

    if response.status_code == 200:
        card_info = response.json()
        return card_info["data"]
    else:
        return "Impossible de charger la base de données"


print("   Programme Skream_update : V.1.0   ")
print("  Starting Hand Calculator")
print(" ****************************\n")

db = load_ygo_db()

# deck: edite decklist = [put the main of your .ydk file here]
decklist = [
    49036338, 94145021, 94145021, 94145021, 95500396,
    23434538, 23434538, 23434538, 38814750, 38814750,
    82224646, 83334932, 83334932, 83334932, 14558127,
    14558127, 14558127, 78391364, 90361010, 90361010,
    92746535, 92746535, 40318957, 40318957, 58092907,
    28720123, 28720123, 56347375, 56347375, 56347375,
    92332424, 92332424, 92332424, 82112494, 82112494,
    82112494, 56727340, 17330916, 76794549, 10604644,
    19510093, 16306932, 16306932, 27813661, 84792926
]

# input
carte_input = input("Quelle carte souhaitez-vous tirer (Veuillez entrer l'ID ou le nom exact de la carte) ? >>> ")

# ID or name
if carte_input.isdigit():
    card_want = int(carte_input)
else:
   # if chars
    want = []
    for card_id in decklist:
        if carte_input in get_card_name(card_id):
            want.append(card_id)
    
    if not want:
        print(f"Carte '{carte_input}' non trouvée dans le deck.")
        exit()
    
    # rand value
    card_want = random.choice(want)

nb_tirage = int(input("Combien de tirages voulez-vous effectuer ? >>> "))
nb_draw = 0
tirage = []

# tirage
for _ in range(nb_tirage):
    main = random.sample(decklist, 5)

    for card_id in main:
        card_name = get_card_name(card_id)
        if card_id == card_want:
            nb_draw += 1
            tirage.append(card_name)

    print("Main tirée :", end=" ")
    for card_id in main:
        print(get_card_name(card_id), end=" ")
    print("")
    print("----------------------------\n")

    
    #decklist = [card_id for card_id in decklist if card_id not in main]

pourcentage = nb_draw / nb_tirage * 100
print(f"{get_card_name(card_want)} a {pourcentage:.2f}% de chance d'être piochée sur {nb_tirage}-tirage")