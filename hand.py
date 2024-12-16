from deck import Deck

class Hand:
    
    def __init__(self, deck):
        self.cards = []
        self.deck = deck
        self.value = 0


    def get_hand(self):
        return self.cards
    

    def draw(self):
        self.cards.append(self.deck.draw_card())


    def draw_two(self):
        self.draw()
        self.draw()


    def get_hand_value(self):
        self.value = 0
        for card in self.cards:
            self.value += card.get_value()
        return self.value


    def print_hand(self):
        for card in self.cards:
            print(card.get_name())
    

    def print_dealer(self):
        for card in self.cards[1:]:
            print(card.get_name())