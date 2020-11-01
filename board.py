#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pieces.pawn import Pawn

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
            [Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v")],
            [None,Pawn("v"),None,None,None,None,None,Pawn("v"),None],
            [Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v")],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^")],
            [None,Pawn("^"),None,None,None,None,None,Pawn("^"),None],
            [Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^")],
        ]


    """ Make a move on the board from (x,y) to (x,y) """
    def make_move (self, player, from_x, from_y, to_x, to_y):
        #TODO
        #After we made a move, we have to chage the turn to another player
        self.player = player._change_turn()
        
