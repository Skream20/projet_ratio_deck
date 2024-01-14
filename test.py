import random

List_val = []


def input_v(hand_size):
    for i in range(hand_size):
        value = int(input(f"Entrez la valeur virtuelle de la carte {i + 1} (1-75): "))
        List_val.append(value)


# Factorial Function
def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)


# Probability Calculation Function
def calculer_probabilite(nb_max, nb, *values):
    try:
        if nb == 5 or nb == 6:
            proba_combinaison = [
                0
            ] * 7  # Initialize a list to store probabilities for 0 to 6 specified cards
            for _ in range(100000):  # Simulating 100,000 draws
                hand = random.sample(range(1, nb_max + 1), nb)
                count_specified_cards = sum(1 for val in values if val in hand)
                proba_combinaison[count_specified_cards] += 1

            for i in range(7):
                proba_combinaison[i] = (proba_combinaison[i] / 100000) * 100
                print(
                    f"La probabilité d'avoir {i} cartes spécifiées dans une main de {nb} cartes dans un deck de {nb_max} cartes est : {proba_combinaison[i]:.2f}%"
                )
        else:
            print(f"Veuillez entrer une taille de main valide (5 ou 6).")

    except ValueError:
        print("Veuillez entrer des valeurs valides.")
        no_yes()


# Execution Function
def exe_proba():
    nb_max = int(input("Entrez le nombre maximal dans le deck : "))
    hand_size = int(input("Entrez la taille de la main (5 ou 6) : "))
    input_v(hand_size)
    if hand_size == 5 or hand_size == 6:
        calculer_probabilite(nb_max, hand_size, *List_val)
    else:
        print("Veuillez entrer une taille de main valide (5 ou 6).")


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
