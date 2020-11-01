#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .piece import Piece

# This class represent a Lance
class Lance(Piece):
    piece_type = "L"

    """ Object constructor """
    def __init__(self, color):
        super().__init__(color)

    """ A lance (L) moves one or more squares straight forward. It cannot moves backwards or to the side.  """
    def correct_move(self, from_x, from_y, to_x, to_y):
        if (from_x < to_x) and (from_y == to_y):
            return True
        else:
            return False