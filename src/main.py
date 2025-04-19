import random
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
    
    # Evaluate the hands
    card = player_hand[0]
    



main()