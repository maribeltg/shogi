#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .piece import Piece

# This class represent a Knight
class Knight(Piece):
    piece_type = "N"

    """ Object constructor """
    def __init__(self, color):
        super().__init__(color)

    """ A knight (N) jumps at an angle intermediate to orthogonal and diagonal, amounting to one square straight forward plus one square diagonally forward, in a single move."""
    def correct_move(self, from_x, from_y, to_x, to_y):
        if ((from_x + 2) == to_x) and (((from_y -1) == to_y) or ((from_y +1) == to_y)) :
            return True
        else:
            return False