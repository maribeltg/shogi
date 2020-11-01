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
            [Lance("v"),Knight("v"),Silver("v"),Gold("v"),King("v"),Gold("v"),Silver("v"),Knight("v"),Lance("v")],
            [None,Rook("v"),None,None,None,None,None,Bishop("v"),None],
            [Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v")],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^")],
            [None,Bishop("^"),None,None,None,None,None,Rook("^"),None],
            [Lance("^"),Knight("^"),Silver("^"),Gold("^"),King("^"),Gold("^"),Silver("^"),Knight("^"),Lance("^")],
        ]


    """ Make a move on the board from (x,y) to (x,y) """
    def make_move (self, player, from_x, from_y, to_x, to_y):
        #TODO
        #After we made a move, we have to chage the turn to another player
        self.player = player._change_turn()
        
