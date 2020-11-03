#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shogi_constants import PLAYER_1, PLAYER_2

# This class represent a player in the game
class Player:
    player1 = PLAYER_1
    player2 = PLAYER_2
    winner_player = False
    current_player = None
    captured = []

    """ Object constructor """
    def __init__(self):
        self.current_player = self.player1

    """ Switches the turn """
    def change_turn(self):
        print(self.current_player)
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    """ Returns the current player """
    def return_turn(self):
        return self.current_player

    """ Returns winner """
    def winner_found(self):
        return self.winner_player

    """ Return the number of captured pieces """
    def get_captured(self):
        return len(self.captured)

