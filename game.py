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
        self.dealer_hand.print_dealer()


    def get_input(self):
        choices = ['h', 's']
        while True:
            print('Do you want to hit or stand?')
            choice = input('(h) or (s): ')
            if choice not in choice:
                print("That's not a valid choice.")
            else:
                return choice


    def dealer_turn(self):
        if self.dealer_hand.get_hand_value() <= 17:
            self.dealer_hand.draw()
            print("Dealer draws")
            self.dealer_hand.print_dealer()
        else:
            print("Dealer stands.")
            return True


    def check_player_bust(self):
        if self.player_hand.get_hand_value() > 21:
            if self.player_hand.check_aces() > 0:
                self.player_hand.value -= 10
                return False
            else:
                return True
        else:
            return False


    def check_dealer_bust(self):
        if self.dealer_hand.get_hand_value() > 21:
            if self.dealer_hand.check_aces() > 0:
                self.dealer_hand.value -= 10
                return False
            else:
                return True
        else:
            return False


    def game_loop(self):
        while True:
            # Player's turn
            choice = self.get_input()
            if choice == 'h':
                self.player_hand.draw()
                self.player_hand.print_hand()
                if self.check_player_bust():
                    print("You busted!")
                    break

            elif choice == 's':
                print("Your score is: " + str(self.player_hand.get_hand_value()))
            
            # Dealer's turn
            dealer_choice = self.dealer_turn()
            if dealer_choice:
                if self.check_dealer_bust():
                    print("The dealer busts!")
                    break
                break               


    def reveal_dealer_hand(self):
        print("The Dealer reveals his hand: ")
        self.dealer_hand.print_hand()
        print("The Dealer's score is: " + str(self.dealer_hand.get_hand_value()))