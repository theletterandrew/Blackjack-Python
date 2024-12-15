class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.value = 0
    
    def get_name(self):
        return self.face + ' of ' + self.suit

    def get_value(self):
        if self.face == 'A':
            self.value = 11
        elif self.face == '2':
            self.value = 2
        elif self.face == '3':
            self.value = 3
        elif self.face == '4':
            self.value = 4
        elif self.face == '5':
            self.value = 5
        elif self.face == '6':
            self.value = 6
        elif self.face == '7':
            self.value = 7
        elif self.face == '8':
            self.value = 8
        elif self.face == '9':
            self.value = 9
        elif self.face == '10' or self.face == 'K' or self.face == 'Q' or self.face == 'J':
            self.value = 10
        return self.value