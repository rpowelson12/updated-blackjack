import random
from cards import Card
from deck import Deck

def main():
    # Creating the deck and shuffling
    deck = Deck()
    shuffled_deck = deck.create_deck()

    # Deal the hands
    player_hand = []
    dealer_hand = []
    while len(player_hand) < 2:
        player_hand.append(shuffled_deck.pop())
        dealer_hand.append(shuffled_deck.pop())

    player_turn(player_hand)

    # winner = determine_winner(player_hand, dealer_hand)

    # print(winner)


# Evaluate the hands
def evaluate_hand(hand):
    length = len(hand)
    total = 0
    for i in range(length):
        card = hand[i]        
        total += card.values[card.rank]
    
    return total

def determine_winner(player, dealer):
    player_total = evaluate_hand(player)
    dealer_total = evaluate_hand(dealer)
    if dealer_total > player_total:
        return "Dealer Wins"
    if dealer_total < player_total:
        return "Player Wins"
    
def player_turn(player):
    total = evaluate_hand(player)
    print(f"Player total is: {total}")
    input(f"Hit or Stay?: ")

main()