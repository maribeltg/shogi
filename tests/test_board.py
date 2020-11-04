#!/usr/bin/env python
# -*- coding: utf-8 -*-
from board import Board
from pieces.lance import Lance
from pieces.knight import Knight
from pieces.silver import Silver
from pieces.gold import Gold
from pieces.king import King
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.pawn import Pawn
from player import Player
from pieces.piece import Piece
from shogi_constants import PLAYER_1 as p1, PLAYER_2 as p2


def test_silver_movement():
    from_x = 4
    from_y = 4
    to_x = 5
    to_y = 3
    board = Board()
    board.state = [
        [Lance(p1),Knight(p1),None,Gold(p1),King(p1),Gold(p1),Silver(p1),Knight(p1),Lance(p1)],
            [None,Rook(p1),None,None,None,None,None,Bishop(p1),None],
            [Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1),Pawn(p1)],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,Silver(p1),None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2),Pawn(p2)],
            [None,Bishop(p2),None,None,None,None,None,Rook(p2),None],
            [Lance(p2),Knight(p2),Silver(p2),Gold(p2),King(p2),Gold(p2),Silver(p2),Knight(p2),Lance(p2)],
    ]
    selected_piece = board.state[from_x][from_y]
    # If the target position (to_x_y) is on the board, we check if the selected piece can make the move
    if selected_piece.on_board(from_x, from_y, to_x, to_y):
        # Then the board is updated and the turn is changed
        if (selected_piece.correct_move(from_x, from_y, to_x, to_y)):
            board.state[from_x][from_y] = None
            board.state[to_x][to_y] = selected_piece
    # target piece must be equal to selected piece
    assert board.state[5][3].piece_type == "S"
   
def test_change_turn():
    player = Player()
    player.current_player = p1
    player.change_turn()
    assert player.current_player == p2

def test_on_board():
    from_x = 4
    from_y = 0
    to_x = 0
    to_y = 5
    piece = Piece(p1)
    is_on_board = piece.on_board(from_x, from_y, to_x, to_y)
    assert is_on_board == True



