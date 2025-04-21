import random
from cards import Card
from deck import Deck
import time

def main():
    # Creating the deck and shuffling
    deck = Deck()
    shuffled_deck = deck.create_deck()

    # Deal the hands
    player_hand = []
    dealer_hand = []
    while len(player_hand) == len(dealer_hand) and len(player_hand) < 2:
        player_hand.append(shuffled_deck.pop())
        dealer_hand.append(shuffled_deck.pop())
    print(shuffled_deck)
    print(f"Dealer's first card is {dealer_hand[0]}")
    player_total = player_turn(player_hand, shuffled_deck)
    if player_total <= 21 and len(player_hand) > 2:
        dealer_total = dealer_turn(dealer_hand, shuffled_deck)

    dealer_total = dealer_turn(dealer_hand, shuffled_deck)

    winner = determine_winner(player_total, dealer_total)
    print(winner)
    again = input("Do you want to play again? (y / n) ")
    if again.lower() == "y":
        main()


    

# Evaluate the hands
def evaluate_hand(hand):
    length = len(hand)
    total = 0
    for i in range(length):
        card = hand[i]        
        total += card.values[card.rank]
    if total > 21:
        count = check_ace(hand)
        total += count * -10
    
    return total

def determine_winner(player_total, dealer_total):
    if dealer_total > player_total:
        return "Dealer Wins"
    if dealer_total < player_total:
        return "Player Wins"
    
def player_turn(hand, deck):
    total = evaluate_hand(hand)
    print(f"Player total is: {total}")
    if (total == 21):
        print("Blackjack!")
        return total
    player_decision = input(f"Hit(H) or Stay(S)?: ")
    while player_decision.lower() == "h" and total <= 21:
        card = deck.pop()
        hand.append(card)
        if card.rank == "Ace":
            total = evaluate_hand(hand)
            if total > 21:
                total -= 10
        else:
            total = evaluate_hand(hand)
        if (total > 21):
            print("Player busted!")
            return total
        print(f"Player total is: {total}")
        player_decision = input(f"Hit(H) or Stay(S)?: ")
    return total
    
def dealer_turn(hand, deck):
    total = evaluate_hand(hand)
    print(f"Dealers initial total {total}")
    while total < 17:
        print("Dealer taking a card...")
        card = deck.pop()
        hand.append(card)
        total = evaluate_hand(hand)
        
        time.sleep(1.5)
        print(f"The card is.. {card}")
        print(f"dealer total in dealer turn: {total}")
        time.sleep(1.5)
        if total > 21:
            total = evaluate_hand(hand)

    return total

def check_ace(hand):
    count = 0
    for card in hand:
        if card.rank == "Ace":
            count += 1

    return count

if __name__ == '__main__':
    main()