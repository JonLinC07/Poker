import random

class Player:

    def __init__(self, name):
        self.name = name
        self.__hand = []
        self.bankroll = 1000

    def __str__(self):
        player_str = 'Nombre: ' + self.name + '\n' + 'Dinero disponible: ${:,.2f}'.format(self.bankroll)
        return player_str

    def make_players(self):
        players      = []
        num_players  = 8
        player_names = ['adam', 'Scott', 'Michael', 'Andrew', 'Mark', 'Fernando', 'Faith', 'Steve', 
                        'Lee', 'Amani', 'Liv', 'Nick A', 'James', 'Jake', 'Brett', 'Graham', 'Fraser', 
                        'Jacob', 'Chelsea', 'Phil', 'George', 'Charley', 'Emma', 'Steph']

        random.shuffle(player_names)

        for n in range(num_players):
            name   = player_names[n]
            player = Player(name)

            players.append(player)
            player_names.pop(n)
        
        return players

    def recive_card(self, card):
        self.__hand.append(card)

    def show_hand(self):
        return self.__hand


