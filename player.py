#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This class represent a player in the game
class Player:
    player1 = "Black"
    player2 = "White"
    winner_player = None
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

    #""" Dado un jugador, lo pone como ganador """
    #def set_winner(self, winner):
    #    self.winner_player = winner

    #""" Devuelve el jugador ganador """
    #def get_winner(self):
    #    return self.winner_player

    #""" Turno inicial """
    #def _set_new_game(self):
    #    self.current_player = self.player1
    #    self.winner_player = None

    """ Return the number of captured pieces """
    def get_captured(self):
        return len(self.captured)

