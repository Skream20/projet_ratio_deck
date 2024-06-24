import json
import requests
import random
import time
import math
from collections import Counter


def load_ygo_db():
    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    response = requests.get(base_url)
    if response.status_code == 200:
        card_info = response.json()
        return card_info["data"]
    else:
        raise Exception("Impossible de charger la base de données")


def load_card_names(db):
    return {card["id"]: card["name"] for card in db}


def load_decklist(file_path):
    decklist = []
    with open(file_path, "r") as file:
        found_main = False
        for line in file:
            line = line.strip()
            if found_main and line.startswith("#"):
                break
            if found_main:
                decklist.append(int(line))
            elif line.startswith("#main"):
                found_main = True
    return decklist


def record_drawn_hands(decklist, nb_tirage):
    return [random.sample(decklist, 5) for _ in range(nb_tirage)]


def display_most_repeated_hands(tirages, top_n=5):
    counter = Counter(tuple(hand) for hand in tirages)
    return counter.most_common(top_n)


def calculate_card_percentage(card_id, tirages):
    nb_draw = sum(1 for tirage in tirages if card_id in tirage)
    return nb_draw / len(tirages) * 100


def calculate_hand_probability(cards, tirages, num_cards):
    successful_draws = 0
    for hand in tirages:
        if sum(card_id in hand for card_id in cards) == num_cards:
            successful_draws += 1
    return successful_draws / len(tirages) * 100


def display_options(cards, tirages):
    print("Que souhaitez-vous afficher ?")
    print("1. Pourcentage de chance de piocher une carte spécifique.")
    print("2. Les mains les plus fréquemment tirées.")
    print("3. Probabilité d'avoir un certain nombre de cartes précises dans la main.")

    choice = input("Entrez votre choix (1, 2 ou 3) : ")
    
    if choice == '1':
        for card_id in cards:
            pourcentage = calculate_card_percentage(card_id, tirages)
            print(f"{card_names[card_id]} a {pourcentage:.2f}% de chance d'être piochée sur {nb_tirage}-tirage")
    elif choice == '2':
        most_common_hands = display_most_repeated_hands(tirages)
        print("Les mains les plus fréquemment tirées :")
        for i, (hand, count) in enumerate(most_common_hands, 1):
            print(f"Main {i} avec {count} répétitions : {[card_names[card_id] for card_id in hand]}")
    elif choice == '3':
        num_cards = int(input("Entrez le nombre de cartes précises que vous souhaitez avoir dans la main : "))
        prob = calculate_hand_probability(cards, tirages, num_cards)
        print(f"Probabilité d'avoir exactement {num_cards} cartes précises dans la main : {prob:.2f}%")
    else:
        print("Choix invalide.")


print("   Programme Skream_update : V.1.0   ")
print("  Starting Hand Calculator")
print(" ****************************\n")

db = load_ygo_db()
card_names = load_card_names(db)

# Charger le fichier .ydk
while True:
    file_path = input("Veuillez entrer le chemin du fichier .ydk : ")
    try:
        decklist = load_decklist(file_path)
        print("\nContenu du fichier .ydk :\n")
        for card_id in decklist:
            print(f"Carte ID : {card_id}, Nom : {card_names[card_id]}")
        break
    except FileNotFoundError:
        print("Fichier non trouvé. Veuillez entrer un chemin de fichier valide.")

cartes_input = input("Quelles cartes souhaitez-vous tirer (Veuillez entrer les IDs ou les noms exacts des cartes, séparés par des virgules) ? >>> ")
cards_want = []
for carte_input in cartes_input.split(","):
    if carte_input.isdigit():
        cards_want.append(int(carte_input))
    else:
        matches = [card_id for card_id in decklist if carte_input in card_names[card_id]]
        if not matches:
            print(f"Carte '{carte_input}' non trouvée dans le deck.")
            continue
        cards_want.extend(matches)

nb_tirage = math.comb(len(decklist), 5)

start_time = time.time()  # Start time

tirages = record_drawn_hands(decklist, nb_tirage)

end_time = time.time()  # End time

# Afficher les options pour l'utilisateur
display_options(cards_want, tirages)

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
    file.write("Pourcentages de chance de piocher chaque carte spécifique :\n")
    for card_id in cards_want:
        file.write(f"{card_names[card_id]} : {calculate_card_percentage(card_id, tirages):.2f}%\n")
    file.write("----------------------------------\n")
    file.write("Les mains les plus fréquemment tirées :\n")
    for i, (hand, count) in enumerate(display_most_repeated_hands(tirages), 1):
        file.write(f"Main {i} avec {count} répétitions : {[card_names[card_id] for card_id in hand]}\n")
