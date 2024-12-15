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


    def get_input(self):
        choices = ['h', 's']
        while True:
            print('Do you want to hit or stand?')
            choice = input('(h) or (s): ')
            if choice not in choice:
                print("That's not a valid choice.")
            else:
                return choice


    def game_loop(self):
        while True:
            choice = self.get_input()
            if choice == 'h':
                self.player_hand.draw()
                self.player_hand.print_hand()

            elif choice == 's':
                print("Your score is: " + str(self.player_hand.get_hand_value()))
                break
            
            