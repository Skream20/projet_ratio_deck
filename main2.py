import random
def calculer_probabilite():
    try:
        value = int(input("Entrez une valeur (entre 1 - 75) : "))
        nb_max = int(input("Entrez le nombre maximal dans le deck : "))

        if 1 <= value <= 75:
            proba = value / nb_max * 100
            print(f"La probabilité d'obtenir la carte {value} dans un deck de {nb_max} cartes est : {proba:.2f}%")
        else:
            print("Veuillez entrer une valeur entre 1 et 75.")

    except ValueError:
        print("Veuillez entrer des valeurs valides.")
        no_yes()

def no_yes():
    answer = input("do you want to restart? [y/n]")
    if answer == "y" or answer == "yes":
        calculer_probabilite()
    elif answer == "n" or answer == "no":
        exit()
    else:
        print("input error!")
        
def hand_tester(taille_main):
    nom_fichier = "list.txt"
    try:
        with open(nom_fichier, 'r') as file:
            contenu = file.read().replace('\n', '')
       
        valeurs = [int(char) for char in contenu if char.isdigit()]

        main_tiree = random.sample(valeurs, min(taille_main, len(valeurs)))
        print(f"Combinaison de {taille_main} cartes tirée aléatoirement : {main_tiree}")

    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as error:
        print(f"Une erreur s'est produite : {error}")


def affichage():
    #hand_tester(5)
    print(calculer_probabilite())
    
print(affichage())


