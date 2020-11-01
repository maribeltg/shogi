#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from sogui_constants import BOARD_SIZE
#from pawn import Pawn
BOARD_SIZE = 9

# This class represent one piece of the game
class Piece:
    color = None #^ is black and v is white
    piece_type = None #Object of type King(K), GoldGeneral(G), SilverGeneral(S), Knights(N), Lances(L), Bishop(B), Rook(R), Pawns(P)
    promoted = False

    """ Object constructor """
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.piece_type + self.color

    """ This method raises a exception if the destination coordinates are out of the board"""
    def on_board(self, from_x, from_y, to_x, to_y):
        if (to_x < 0) or (to_x >= BOARD_SIZE):
            raise Exception ("Invalid coordinates. The board size is 9x9. ")
        if (to_y < 0) or (to_y >= BOARD_SIZE):
            raise Exception ("Invalid coordinates. Tha board size is 9x9. ")
        else:
            return True
