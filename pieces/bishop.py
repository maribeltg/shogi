#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .piece import Piece

# This class represent a Bishop
class Bishop(Piece):
    piece_type = "B"

    """ Object constructor """
    def __init__(self, color):
        super().__init__(color)

    """ A bishop (B) moves any number of squares in a diagonal direction """
    def correct_move(self, from_x, from_y, to_x, to_y):
        #TODO
        if ((from_x + 1) == to_x) and (from_y == to_y):
            return True
        else:
            return False