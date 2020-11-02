#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .piece import Piece

# This class represent a Pawn
class Rook(Piece):
    piece_type = "R"

    """ Object constructor """
    def __init__(self, color):
        super().__init__(color)

    """ A Rook (R) moves any number of squares in an orthogonal direction. """
    def correct_move(self, from_x, from_y, to_x, to_y):
        if (from_x == to_x) or (from_y == to_y):
            return True
        else:
            return False