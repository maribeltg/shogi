#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .piece import Piece

# This class represent a Pawn
class Pawn(Piece):
    piece_type = "P"

    """ Object constructor """
    def __init__(self, color):
        super().__init__(color)

    """ A pawn (P) moves one square straight forward. It cannot retreat. """
    def correct_move(self, from_x, from_y, to_x, to_y):
        if (self.color == "v"):
            if ((from_x + 1) == to_x) and (from_y == to_y):
                return True
            else:
                return False
        else:
            if ((from_x - 1) == to_x) and (from_y == to_y):
                return True
            else:
                return False

