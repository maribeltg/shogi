#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .piece import Piece

# This class represent a Gold General
class Gold(Piece):
    piece_type = "G"

    """ Object constructor """
    def __init__(self, color):
        super().__init__(color)

    """A Gold General moves one square orthogonally, or one square diagonally forward """
    def correct_move(self, from_x, from_y, to_x, to_y):
        #TODO
        if (((from_x + 1) == to_x) and ((from_y - 1) == to_y)) or  (((from_x + 1) == to_x) and (from_y == to_y)) or (((from_x + 1) == to_x) and ((from_y + 1) == to_y)) or (((from_x - 1) == to_x) and ((from_y -1) == to_y)) or (((from_x + 1) == to_x) and ((from_y + 1) == to_y)):
            return True
        else:
            return False