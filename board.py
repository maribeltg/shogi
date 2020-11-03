#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pieces.pawn import Pawn
from pieces.lance import Lance
from pieces.knight import Knight
from pieces.silver import Silver
from pieces.gold import Gold
from pieces.king import King
from pieces.rook import Rook
from pieces.bishop import Bishop
from shogi_constants import PLAYER_1 as p1, PLAYER_2 as p2


# This class represent the board of the game
class Board:
    player = None
    state = None
    from_x = None
    from_y = None
    to_x = None
    to_y = None

    """ Object constructor """
    def __init__(self):
        self.state = [
            [Lance(p1),Knight(p1),Silver(p1),Gold(p1),King(p1),Gold(p1),Silver(p1),Knight(p1),Lance(p1)],
            [None,Rook(p1),None,None,None,None,None,Bishop(p1),None],
            [Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1)],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2)],
            [None,Bishop(p2),None,None,None,None,None,Rook(p2),None],
            [Lance(p2),Knight(p2),Silver(p2),Gold(p2),King(p2),Gold(p2),Silver(p2),Knight(p2),Lance(p2)],
        ]


    """ Make a move on the board from (x,y) to (x,y) """
    def make_move (self, player, from_x, from_y, to_x, to_y):
        #After we made a move, we have to chage the turn to another player
        self.player = player._change_turn()
        
