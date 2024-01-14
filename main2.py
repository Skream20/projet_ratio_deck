import random
from math import comb

List_val = []


def input_v(nb):
    if nb == 6:
        value0 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value1 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value2 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value3 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value4 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value5 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        List_val.extend([value0, value1, value2, value3, value4, value5])
    elif nb == 5:
        value0 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value1 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value2 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value3 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value4 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        List_val.extend([value0, value1, value2, value3, value4])
    elif nb == 4:
        value0 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value1 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value2 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value3 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        List_val.extend([value0, value1, value2, value3])
    elif nb == 3:
        value0 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value1 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value2 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        List_val.extend([value0, value1, value2])
    elif nb == 2:
        value0 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        value1 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        List_val.extend([value0, value1])
    else:
        value0 = int(input("Entrez valeur virtuel de la carte(1-75): "))
        List_val.extend([value0])


# calcule
def calculer_probabilite(nb_max, nb, *values):
    try:
        if nb == 1:
            proba = List_val[0] / nb_max * 100
            print(
                f"La probabilité d'obtenir la carte {List_val[0]} dans un deck de {nb_max} cartes est : {proba:.2f}%"
            )
        elif nb == 2:
            proba = (List_val[0] / nb_max) * (List_val[1] / nb_max) * 100
            print(
                f"La probabilité d'obtenir les cartes {List_val[0]} et {List_val[1]} dans un deck de {nb_max} cartes est : {proba:.2f}%"
            )
        elif nb == 3:
            proba = (
                (List_val[0] / nb_max)
                * (List_val[1] / nb_max)
                * (List_val[2] / nb_max)
                * 100
            )
            print(
                f"La probabilité d'obtenir les cartes {List_val[0]}, {List_val[1]} et {List_val[2]} dans un deck de {nb_max} cartes est : {proba:.2f}%"
            )
        elif nb == 4:
            proba = (
                (List_val[0] / nb_max)
                * (List_val[1] / nb_max)
                * (List_val[2] / nb_max)
                * (List_val[3] / nb_max)
                * 100
            )
            print(
                f"La probabilité d'obtenir les cartes {List_val[0]}, {List_val[1]}, {List_val[2]} et {List_val[3]} dans un deck de {nb_max} cartes est : {proba:.2f}%"
            )
        elif nb == 5:
            proba = (
                (List_val[0] / nb_max)
                * (List_val[1] / nb_max)
                * (List_val[2] / nb_max)
                * (List_val[3] / nb_max)
                * (List_val[4] / nb_max)
                * 100
            )
            print(
                f"La probabilité d'obtenir les cartes {List_val[0]}, {List_val[1]}, {List_val[2]}, {List_val[3]} et {List_val[4]} dans un deck de {nb_max} cartes est : {proba:.2f}%"
            )
        elif nb == 6:
            proba = (
                (List_val[0] / nb_max)
                * (List_val[1] / nb_max)
                * (List_val[2] / nb_max)
                * (List_val[3] / nb_max)
                * (List_val[4] / nb_max)
                * (List_val[5] / nb_max)
                * 100
            )
            print(
                f"La probabilité d'obtenir les cartes {List_val[0]}, {List_val[1]}, {List_val[2]}, {List_val[3]}, {List_val[4]} et {List_val[5]} dans un deck de {nb_max} cartes est : {proba:.2f}%"
            )
        else:
            print(f"Veuillez entrer une valeur entre 1 et 75 pour {nb}.")

    except ValueError:
        print("Veuillez entrer des valeurs valides.")
        no_yes()


# restart function
def no_yes():
    answer = input("Do you want to restart? [y/n]")
    if answer == "y" or answer == "yes":
        exe_proba()
    elif answer == "n" or answer == "no":
        exit()
    else:
        print("Input error!")


# execution function
def exe_proba():
    nb_max = int(input("Entrez le nombre maximal dans le deck : "))
    nb = int(input("Nombre de cartes à avoir en main:"))
    input_v(nb)
    calculer_probabilite(nb_max, nb, *List_val)


# Example usage
exe_proba()


# restart function
def no_yes():
    answer = input("Do you want to restart? [y/n]")
    if answer == "y" or answer == "yes":
        exe_proba()
    elif answer == "n" or answer == "no":
        exit()
    else:
        print("Input error!")


# hand test
def hand_tester(taille_main):
    nom_fichier = "list.txt"
    try:
        with open(nom_fichier, "r") as file:
            contenu = file.read().replace("\n", "")
        value = 0

        main_tiree = random.sample(value, min(taille_main, len(value)))
        print(f"Combinaison de {taille_main} cartes tirée aléatoirement : {main_tiree}")

    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as error:
        print(f"Une erreur s'est produite : {error}")
