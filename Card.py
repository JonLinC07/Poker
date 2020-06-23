class Card:
        
    def __init__(self, value, kind, name, image):
        self.value = value
        self.kind  = kind
        self.name  = name
        self.image = image 
    
    def __str__(self):
        return self.image

    @staticmethod
    def create_deck():
            cards       = []
            values      = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            kinds       = ['♥', '♦', '♣', '♠']
            kinds_names = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            names       = ['A', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'J', 'Q', 'K']

            for kind in kinds:
                for value in values:
                    name  = names[values.index(value)]
                    
                    if value == 1 or value == 11 or value == 12 or value == 13:
                        image = '|' + name + ' ' + kind + '|'
                    else:
                        image = '|' + str(value) + ' ' + kind + '|'

                    card = Card(value, kind, name, image)
                    cards.append(card)
            
            return cards
