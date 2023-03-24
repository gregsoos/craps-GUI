"""
File: die.py
Author: Greg Soos
Last modified: 3/24/2023

This module defines the Die class. It creates a six-sided die object that can roll.
"""

from random import randint


class Die:
    """Creates a six-sided die that can roll, and whose value can be retrieved."""

    def __init__(self):
        """Initialize value of die as a 1."""
        self.value = 1

    def roll(self):
        """Roll die, returning int value between 1 and 6."""
        self.value = randint(1, 6)
        return self.value

    def __str__(self):
        """Return value of die as a string."""
        return str(self.value)
