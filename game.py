class Game:
    
    def __init__(self, player_hand, dealer_hand):
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand


    def new_game(self):
        self.player_hand.draw_two()
        print('You draw: ')
        self.player_hand.print_hand()

        self.dealer_hand.draw_two()
        print('Dealer shows: ')
        self.dealer_hand.print_one()


    def game_loop(self):
        choices = ['h', 's']
        while True:
            print('Do you want to hit or stand? ')
            choice = input('(h) or (s): ')
            if choice not in choices:
                print("That's not a choice.")
            elif choice == 'h':
                self.player_hand.draw()
                self.player_hand.print_hand()