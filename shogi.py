#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" author: Maribel Tirados Gomez
"""
import sys
from draw_board import DrawBoard
from board import Board
from player import Player
# Main 
class Main:
    """Constructor"""
    def __init__(self):
        #Creating the player en the board
        player = Player()
        board = Board()

        #Drawing the board and the turn on the console
        DrawBoard._draw_board(board)
        DrawBoard._draw_turn(player)

        #Get the coordinates from the user
        from_x_y = input("From (row col):")
        to_x_y = input("To (row col):")
        from_list = from_x_y.split()
        to_list = to_x_y.split()

        #Get the selected piece
        selected_piece = board.state[int(from_list[0])][int(from_list[1])]

        # If the target position (to_x_y) is on the board, we check if the selected piece can make the move
        if selected_piece._on_board(int(from_list[0]), int(from_list[1]), int(to_list[0]), int(to_list[1])):
            # Then the board is updated and the turn is changed
            if (selected_piece._correct_move(int(from_list[0]), int(from_list[1]), int(to_list[0]), int(to_list[1]))):
                board.state[int(from_list[0])][int(from_list[1])] = None
                board.state[int(to_list[0])][int(to_list[1])] = selected_piece
                player._change_turn()
                DrawBoard._draw_board(board)
                DrawBoard._draw_turn(player)
    
if __name__ == "__main__":
    main = Main()


