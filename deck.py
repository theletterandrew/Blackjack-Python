from card import Card

import random

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def new_deck(self):
        FACES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        SUITS = ['spades', 'hearts', 'diamonds', 'clubs']

        for face in FACES:
            for suit in SUITS:
                self.add_card(Card(face, suit))

    def get_cards(self):
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
    