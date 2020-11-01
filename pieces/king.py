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
        #TODO
        if ((from_x + 1) == to_x) and (from_y == to_y):
            return True
        else:
            return False