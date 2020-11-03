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
        while not(player.winner_found()):
            try:
                #Drawing the board and the turn on the console
                DrawBoard.draw_board(board)
                DrawBoard.draw_turn(player)
                DrawBoard.draw_captured(player)

                #Return the player's last captured piece.
                if (len(player.get_captured()) > 0):
                    return_piece = input("Do you want to return a captured piece?(yes/no)")
                    if (return_piece == "yes"):
                        to_x_y = input("To (row col):")
                        to_list = to_x_y.split()
                        selected_target = board.state[int(to_list[0])][int(to_list[1])]
                        #Check empty square
                        if not selected_target:
                            recovered_piece = player.get_captured().pop()
                            recovered_piece.color = player.current_player
                            board.state[int(to_list[0])][int(to_list[1])] = recovered_piece                            
                            player.change_turn()
                            continue
                        


                #Get the coordinates from the user
                from_x_y = input("From (row col):")
                to_x_y = input("To (row col):")
                from_list = from_x_y.split()
                to_list = to_x_y.split()

                #Get the selected piece
                selected_piece = board.state[int(from_list[0])][int(from_list[1])]
                selected_target = board.state[int(to_list[0])][int(to_list[1])]

                #Both selected piece and current player has to have the same color
                if (selected_piece.color == player.current_player):
                    # If the target position (to_x_y) is on the board, we check if the selected piece can make the move
                    if selected_piece.on_board(int(from_list[0]), int(from_list[1]), int(to_list[0]), int(to_list[1])):
                        # Then the board is updated and the turn is changed
                        if (selected_piece.correct_move(int(from_list[0]), int(from_list[1]), int(to_list[0]), int(to_list[1]))):
                            #if to_x_y has a piece and the color is the opponent's color, the piece is captured
                            if (selected_target) and (selected_target.color != selected_piece.color):
                                player.set_captured(selected_target)
                            board.state[int(from_list[0])][int(from_list[1])] = None
                            board.state[int(to_list[0])][int(to_list[1])] = selected_piece
                            player.change_turn()
        
                else:
                    raise Exception ()
            except (KeyboardInterrupt, SystemExit):
                raise
            except Exception as e:
                print(e)
                print("----------Incorrect movement. ")    

            
if __name__ == "__main__":
    main = Main()


