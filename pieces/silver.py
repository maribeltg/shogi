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
        """ The King movement has been used as a template. """
        if (abs(from_x - to_x) <= 1 and abs(from_y - to_y) <= 1 and from_x != to_x and from_y != to_y):
            if (self.color == "v"):  
                if (from_x == to_x) or ((from_x - 1 == to_x) and (from_y == to_y)): #invalid squares
                    return False
                else:
                    return True
            else:
                if (from_x == to_x) or ((from_x +1 == to_x) and (from_y == to_y)): #invalid squares
                    return False
                else:
                    return True
        else:
            False


