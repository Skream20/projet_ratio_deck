from math import comb

# Number of "one card combo" cards in the deck
one_card_combo_cards = 12

# Number of "ht" cards in the deck
ht_cards = 9

# Total number of cards in the deck
total_cards = 40

# Number of cards to draw in the hand (either 6 or 5)
hand_size_6 = 6
hand_size_5 = 5

# Calculate the probability of drawing "one card combo" in a hand of 6 cards
prob_one_card_combo_6 = (
    comb(one_card_combo_cards, 1) / comb(total_cards, hand_size_6)
) * (
    comb(total_cards - one_card_combo_cards, hand_size_6 - 1)
    / comb(total_cards, hand_size_6 - 1)
)

# Calculate the probability of drawing "ht" in a hand of 6 cards
prob_ht_6 = (comb(ht_cards, 1) / comb(total_cards, hand_size_6)) * (
    comb(total_cards - ht_cards, hand_size_6 - 1) / comb(total_cards, hand_size_6 - 1)
)

# Calculate the probability of drawing "one card combo" in a hand of 5 cards
prob_one_card_combo_5 = (
    comb(one_card_combo_cards, 1) / comb(total_cards, hand_size_5)
) * (
    comb(total_cards - one_card_combo_cards, hand_size_5 - 1)
    / comb(total_cards, hand_size_5 - 1)
)

# Calculate the probability of drawing "ht" in a hand of 5 cards
prob_ht_5 = (comb(ht_cards, 1) / comb(total_cards, hand_size_5)) * (
    comb(total_cards - ht_cards, hand_size_5 - 1) / comb(total_cards, hand_size_5 - 1)
)

# Print the results
print(
    "Probability of drawing 'one card combo' in a hand of 6 cards: {:.2%}".format(
        prob_one_card_combo_6
    )
)
print("Probability of drawing 'ht' in a hand of 6 cards: {:.2%}".format(prob_ht_6))
print(
    "Probability of drawing 'one card combo' in a hand of 5 cards: {:.2%}".format(
        prob_one_card_combo_5
    )
)
print("Probability of drawing 'ht' in a hand of 5 cards: {:.2%}".format(prob_ht_5))
