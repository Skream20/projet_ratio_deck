import random
import math

List_val = []


def input_v(hand_size):
    for i in range(hand_size):
        value = int(input(f"Entrez la valeur virtuelle de la carte {i + 1} (1-75): "))
        List_val.append(value)


# calcule
def calculer_probabilite(nb_max, nb, *values):
    try:
        if nb < 1 or nb > 6:
            raise ValueError("Le nombre de cartes doit être entre 1 et 6.")

        if len(values) != nb:
            raise ValueError(f"Le nombre de valeurs doit être égal à {nb}.")

        proba = 1.0
        for val in values:
            if val < 1 or val > nb_max:
                raise ValueError(
                    "Les valeurs des cartes doivent être entre 1 et le nombre maximal dans le deck."
                )
            proba *= 1 / nb_max

        proba *= math.factorial(nb_max) / math.factorial(nb_max - nb)

        proba *= 100
        print(
            f"La probabilité d'obtenir les cartes {', '.join(map(str, values))} "
            f"dans une main de {nb} cartes dans un deck de {nb_max} cartes est : {proba:.2f}%"
        )

    except ValueError as e:
        print(f"Erreur : {e}")
        no_yes()


# Execution Function
def exe_proba():
    nb_max = int(input("Entrez le nombre maximal dans le deck : "))
    hand_size = int(input("Entrez la taille de la main (5 ou 6) : "))
    input_v(hand_size)
    calculer_probabilite(nb_max, hand_size, *List_val)


# Restart Function
def no_yes():
    answer = input("Do you want to restart? [y/n]")
    if answer == "y" or answer == "yes":
        exe_proba()
    elif answer == "n" or answer == "no":
        exit()
    else:
        print("Input error!")


# Example Usage
exe_proba()
