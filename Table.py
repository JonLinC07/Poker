from Dealer import Dealer
from Player import Player
from Card   import Card

class Table:

    def __init__(self, players, board=[], pot=0):
        self.players = players
        self.board   = board
        self.pot     = pot

    # def table_status(self):
