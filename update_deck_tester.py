import requests
import random

def get_card_name(card_id):
    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    params = {"id": card_id}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        card_info = response.json()
        card_name = card_info["data"][0]["name"]
        return card_name
    else:
        return "Carte non trouvée"

print("   Programme Skream_update : V.1.0   ")
print("  Starting Hand Calculator")
print(" ****************************\n")

#your deck:
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

CarteVoulue = input("Quelle carte souhaitez-vous tirer (Veuillez entrer l'id exact) ? >>> ")
nbTirages = int(input("Combien de tirages voulez-vous effectuer ? >>> "))
nbDeFoisTiree = 0

tirage = []

#va faire piocher les cartes 
for _ in range(nbTirages):
    main = random.sample(decklist, 5)

    for card_id in main:
        card_name = get_card_name(card_id)
        if card_id == CarteVoulue and card_id not in tirage:
            nbDeFoisTiree += 1
            tirage.append(card_name)
        else:
            tirage.append(card_name)
    
    #print("Main tirée :")
    #for card_id in main:
        #card_name = get_card_name(card_id)
        #print(card_name)
        
    #contraction de la boucle for lier à main tirer
    print("Main tirée :", [get_card_name(card_id) for card_id in main])
    
    print("----------------------------\n")
    
    #met à jour la dl sur les carte tirer dans le deck
    U_decklist = []
    for card_id in decklist:
        if card_id not in main:
            U_decklist.append(card_id)
            decklist = U_decklist

print(f"{get_card_name(CarteVoulue)} a été tirée {nbDeFoisTiree} fois")



