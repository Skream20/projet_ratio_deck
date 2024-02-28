import json
import requests
import random
import time
from collections import Counter


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
        return "Impossible de charger la base de données après plusieurs tentatives"


def record_drawn_hands(decklist, nb_tirage):
    tirages = []

    for _ in range(nb_tirage):
        main = random.sample(decklist, 5)
        tirages.append(tuple(main))

    return tirages


def display_most_repeated_hands(tirages, top_n=5):
    counter = Counter(tirages)
    most_common = counter.most_common(top_n)

    print(f"\nLes {top_n} mains les plus fréquemment tirées sont :")
    for i, (hand, count) in enumerate(most_common, 1):
        print(f"Main {i} avec {count} répétitions :", end=" ")
        for card_id in hand:
            print(get_card_name(card_id), end=", ")
        print("")


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

print('\r' + ' ' * 10 + '\r', end='', flush=True)

# input
carte_input = input(
    "Quelle carte souhaitez-vous tirer (Veuillez entrer l'ID ou le nom exact de la carte) ? >>> ")

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

# Record all drawn hands
tirages = record_drawn_hands(decklist, nb_tirage)

# Display each drawn hand

for i, tirage in enumerate(tirages, 1):
    print(f"Main {i} tirée :", end=" ")
    for card_id in tirage:
        print(get_card_name(card_id), end=" ")
    print("")


# Display the percentage for the specified card
nb_draw = sum(1 for tirage in tirages if card_want in tirage)
# Calculate and display the percentage of the most repeated hands
display_most_repeated_hands(tirages)
pourcentage = nb_draw / nb_tirage * 100
print(f"{get_card_name(card_want)} a {pourcentage:.2f}% de chance d'être piochée sur {nb_tirage}-tirage")
