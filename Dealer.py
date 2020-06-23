from Card   import Card
from Player import Player
from random import shuffle

class Dealer:

    def __init__(self):
        self.__deck = Card.create_deck()

    def deal_cards(self, players):

        for n in range(2):
            for player in players:
                card = self.__deck[0]
                player.recive_card(card)

                self.__deck.remove(card)

    def show_deck(self):
        cards = []

        for card in self.__deck:
            cards.append(card.image)
        
        print(cards)

    def shuffle(self):
        shuffle(self.__deck)

