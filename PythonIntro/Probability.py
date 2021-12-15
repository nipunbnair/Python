no_of_sides_in_a_coin = 2
no_of_head = 1
prob_head = no_of_head / no_of_sides_in_a_coin
print("probability of head in coin toss")
print(round(prob_head, 2))
no_of_cards = 52
no_of_aces = 4
prob_ace = no_of_aces / no_of_cards
print("probability of ace in a deck of cards")
print(round(prob_ace, 2))
no_of_dice_phases = 6
no_of6 = 1
prob_6 = no_of6 / no_of_dice_phases
print("probability of getting 6 in die tossed")
print(round(prob_6, 2))
head_percent = prob_head * 100
ace_percent = prob_ace * 100
six_percent = prob_6 * 100
print("Probability percentage of head in coin toss")
print(str(round(head_percent, 0)) + "%")
print("probability percentage of ace in deck of cards")
print(str(round(ace_percent, 0)) + "%")
print("probability percentage of 6 in die tossed")
print(str(round(six_percent, 0)) + "%")


def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100

    return round(probability, 1)


# Sample Space

cards = 52

# Determine the probability of drawing a heart

hearts = 13

heart_probability = event_probability(hearts, cards)

# Determine the probability of drawing a face card

face_cards = 12

face_card_probability = event_probability(face_cards, cards)

# Determine the probability of drawing the queen of hearts

queen_of_hearts = 1

queen_of_hearts_probability = event_probability(queen_of_hearts, cards)

# Print each probability

print(str(heart_probability) + '%')

print(str(face_card_probability) + '%')

print(str(queen_of_hearts_probability) + '%')
cards=52
cards_drawn=1
cards=cards-cards_drawn
aces=4
ace_probability1=event_probability(aces,cards)
aces_drawn=1
aces=aces-aces_drawn
ace_probability2=event_probability(aces,cards)
print(ace_probability1)
print(ace_probability2)
