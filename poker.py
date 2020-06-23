from Dealer import Dealer
from Player import Player

dealer = Dealer()

player_name = input('Ingrese el nombre del jugador \n|>> ')

player  = Player(player_name)
players = player.make_players()

players.append(player)

dealer.shuffle()
dealer.deal_cards(players)

for player in players:
    print(player)

    for card in  player.show_hand():
        print(card)
