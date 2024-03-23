import json
import requests
import random
import time
from collections import Counter


def load_ygo_db():
    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    response = requests.get(base_url)
    if response.status_code == 200:
        card_info = response.json()
        return card_info["data"]
    else:
        return "Impossible de charger la base de données après plusieurs tentatives"


def load_card_names(db):
    return {card["id"]: card["name"] for card in db}


def record_drawn_hands(decklist, nb_tirage):
    tirages = []
    for _ in range(nb_tirage):
        main = random.sample(decklist, 5)
        tirages.append(tuple(main))
    return tirages


def display_most_repeated_hands(tirages, top_n=5):
    counter = Counter(tirages)
    most_common = counter.most_common(top_n)
    result = []
    for i, (hand, count) in enumerate(most_common, 1):
        hand_cards = [card_names[card_id] for card_id in hand]
        result.append((hand_cards, count))
    return result


def print_ydk_content(decklist):
    print("\nContenu du fichier .ydk :\n")
    for card_id in decklist:
        print(f"Carte ID : {card_id}, Nom : {card_names[card_id]}")


print("   Programme Skream_update : V.1.0   ")
print("  Starting Hand Calculator")
print(" ****************************\n")

db = load_ygo_db()
card_names = load_card_names(db)

# Charger le fichier .ydk
while True:
    file_path = input("Veuillez entrer le chemin du fichier .ydk : ")
    try:
        with open(file_path, "r") as file:
            decklist = []
            for line in file:
                line = line.strip()
                if line.startswith("#main"):
                    break
            for line in file:
                line = line.strip()
                if line.startswith("#"):
                    break
                card_id = int(line)
                decklist.append(card_id)
            print_ydk_content(decklist)
            break
    except FileNotFoundError:
        print("Fichier non trouvé. Veuillez entrer un chemin de fichier valide.")

carte_input = input(
    "Quelle carte souhaitez-vous tirer (Veuillez entrer l'ID ou le nom exact de la carte) ? >>> ")
if carte_input.isdigit():
    card_want = int(carte_input)
else:
    want = {
        card_id for card_id in decklist if carte_input in card_names[card_id]}
    if not want:
        print(f"Carte '{carte_input}' non trouvée dans le deck.")
        exit()
    card_want = random.choice(list(want))

nb_tirage = int(input("Combien de tirages voulez-vous effectuer ? >>> "))

start_time = time.time()  # Start time

tirages = record_drawn_hands(decklist, nb_tirage)

end_time = time.time()  # End time

for i, tirage in enumerate(tirages, 1):
    print(f"Main {i} tirée :", end=" ")
    for card_id in tirage:
        print(card_names[card_id], end=" ")
    print("")

nb_draw = sum(1 for tirage in tirages if card_want in tirage)
display_most_repeated_hands(tirages)
pourcentage = nb_draw / nb_tirage * 100
print(
    f"{card_names[card_want]} a {pourcentage:.2f}% de chance d'être piochée sur {nb_tirage}-tirage")

print(f"Temps d'exécution : {end_time - start_time:.4f} secondes")

# Calcul du nombre total de tirages
total_tirages = nb_tirage

# Temps total d'exécution en secondes
temps_execution = end_time - start_time

# Nombre de tirages par seconde
tirages_par_seconde = total_tirages / temps_execution

print(f"Nombre de tirages par seconde : {tirages_par_seconde:.2f}")

# Enregistrer les résultats dans un fichier
with open("resultats.txt", "w") as file:
    file.write("Résultats de la simulation :\n")
    file.write("----------------------------------\n")
    file.write(f"Nombre total de tirages : {total_tirages}\n")
    file.write(f"Temps d'exécution : {temps_execution:.4f} secondes\n")
    file.write(f"Nombre de tirages par seconde : {tirages_par_seconde:.2f}\n")
    file.write(
        f"Pourcentage de chance de tirer la carte '{card_names[card_want]}' : {pourcentage:.2f}%\n")
    file.write("----------------------------------\n")
    file.write("Les mains les plus fréquemment tirées :\n")
    for i, (hand, count) in enumerate(display_most_repeated_hands(tirages), 1):
        file.write(f"Main {i} avec {count} répétitions : {hand}\n")
