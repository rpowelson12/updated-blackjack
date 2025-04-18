from cards import Card
from deck import Deck

def main():

    deck = Deck.create_deck()
    print(repr(deck))

main()