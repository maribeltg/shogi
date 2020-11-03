#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shogi_constants import TURN

# This class show the state of the game on the console
class DrawBoard:    
    """ Draw the current state of the board on the console. """
    @staticmethod
    def draw_board(board):
        print ("    0  1  2  3  4  5  6  7  8")
        print ("+------------------------------+")

        for row_index, row in enumerate(board.state):
            print(row_index,"|", end=' ')
            for elem in row:
                if elem != None:
                    print (elem, end=' ')
                else:
                    print ("__", end=' ')
            print()

    """ Draw the current player on the console. """
    @staticmethod
    def draw_turn (player):
        turn = player.current_player
        print ("TURN",TURN[turn])

    """ Draw the player's number of captured pieces on the console. """
    @staticmethod
    def draw_captured (player):
        captured = player.get_captured()
        print ("Captured",captured)   

