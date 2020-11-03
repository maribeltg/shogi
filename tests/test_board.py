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

def test_always_passes():
    assert True

def test_silver_movement():
    from_x = 4
    from_y = 4
    to_x = 5
    to_y = 3
    board = Board()
    board.state = [
        [Lance("v"),Knight("v"),None,Gold("v"),King("v"),Gold("v"),Silver("v"),Knight("v"),Lance("v")],
            [None,Rook("v"),None,None,None,None,None,Bishop("v"),None],
            [Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v"),Pawn("v")],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,Silver("v"),None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^"),Pawn("^")],
            [None,Bishop("^"),None,None,None,None,None,Rook("^"),None],
            [Lance("^"),Knight("^"),Silver("^"),Gold("^"),King("^"),Gold("^"),Silver("^"),Knight("^"),Lance("^")],
    ]
    selected_piece = board.state[from_x][from_y]
    # If the target position (to_x_y) is on the board, we check if the selected piece can make the move
    if selected_piece.on_board(from_x, from_y, to_x, to_y):
        # Then the board is updated and the turn is changed
        if (selected_piece.correct_move(from_x, from_y, to_x, to_y)):
            board.state[from_x][from_y] = None
            board.state[to_x][to_y] = selected_piece
    # La pieza de destino tiene que ser la misma que la de origen
    assert board.state[5][3].piece_type == "S"
   