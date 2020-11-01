#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .piece import Piece

# This class represent a Silver General
class Silver(Piece):
    piece_type = "S"

    """ Object constructor """
    def __init__(self, color):
        super().__init__(color)

    """A Silver General moves one square diagonally, or one square straight forward. """
    def correct_move(self, from_x, from_y, to_x, to_y):
        #one square straight forward
        #diagonal forward right
        #diagonal forward left
        #diagonal backward right
        #diagonal backward left

        if (((from_x + 1) == to_x) and (from_y == to_y)) or \
        (((from_x + 1) == to_x) and ((from_y - 1) == to_y)) or \
        (((from_x + 1) == to_x) and ((from_y + 1) == to_y)) or \
        (((from_x - 1) == to_x) and ((from_y -1) == to_y)) or \
        (((from_x + 1) == to_x) and ((from_y + 1) == to_y)): 
            return True
        else:
            return False