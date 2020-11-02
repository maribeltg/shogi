#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .piece import Piece

# This class represent a King
class King(Piece):
    piece_type = "K"

    """ Object constructor """
    def __init__(self, color):
        super().__init__(color)

    """ A King moves one square in any direction, orthogonal or diagonal. """
    def correct_move(self, from_x, from_y, to_x, to_y):
        if (abs(from_x - to_x) <= 1 and abs(from_y - to_y) <= 1 and from_x != to_x and from_y != to_y):
            return True
        else:
            return False