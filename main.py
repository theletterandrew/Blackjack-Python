from card import Card
from deck import Deck
from hand import Hand
from game import Game

deck = Deck()

deck.new_deck()
deck.shuffle()

player_hand = Hand(deck)
dealer_hand = Hand(deck)

game = Game(player_hand, dealer_hand)
game.new_game()
game.game_loop()
game.reveal_dealer_hand()