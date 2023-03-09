"""
    :module_name: match
    :module_summary: class that controlls the match rules of a tile-matching game
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import logging
from abc import ABC, abstractmethod

from ..board import GameBoard
from ..tiles import Tile

class MatchCondition(ABC):
    """
        Class that specifies the interface for match rules
        :scan: the 2-unit vector direction to scan a match for
        :equality_rule: the function the determines if two tiles match
   """
    
    def __init__(self, scan: tuple, value: int, equality_rule: callable = Tile.__eq__):
        self._eq = equality_rule
        self._point_value = value
        self._scan_delta = scan

    @abstractmethod
    def check_match(self, board: GameBoard, start_x: int, start_y: int) -> bool:
        """
            Check for a match on the given board starting at the specified position
            :arg board: the board to check a match for
            :arg start_x: the x position the match scan starts at
            :arg start_y: the y position the match scan starts at
            :arg type: GameBoard
            :arg type: int
            :arg type: int
            :returns: True if a match is detected, False otherwise
            :rtype: bool
        """
        LOGGER.warning('Using default implementation. This is meant to be overridden!')
        pass
            
    @property
    def point_value(self) -> int:
        """
            Read only view of the point value of this match condition
            :returns: match condition's point value
            :rtype: int
        """
        LOGGER.debug('Match condition is worth: %d points', self._point_value)
        return self._point_value
