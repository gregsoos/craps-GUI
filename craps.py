"""
File: craps.py
Author: Greg Soos
Last modified: 3/24/2023

This module allows a player to roll dice to play the game of craps.
"""

from die import Die


class Player:
    """Create a player object who can roll a pair of dice to play the game craps."""

    def __init__(self):
        """
        Initialize attributes including objects for both dice and parameters to determine sum of roll,
        how many rolls in the craps game, the value of the first (target) roll, the winner/loser condition,
        and whether this is the first roll.
        """
        self.die1 = Die()
        self.die2 = Die()
        self.addedRoll = 2  # Initialize roll at 2; this is reset upon first roll
        self.firstRoll = 2
        self.rollsCount = 0
        self.atStartup = True  # True value indicates this is the first roll of the game
        self.winner = self.loser = False  # True conditions means the player has won/lost respectively

    def __str__(self):
        """Return sum of dice values as a string. """
        return str(self.addedRoll)

    def rollDice(self):
        """
        Player rolls dice. Roll count increase by one, and winner/loser condition changes to True
        if necessary according to rules of craps.
        """

        if self.atStartup:  # Win/loss condition differs in craps between first roll and successive rolls
            self.addedRoll = self.die1.roll() + self.die2.roll()
            self.firstRoll = self.addedRoll  # Save first roll for successive rolls (if necessary)
            self.rollsCount += 1
            self.atStartup = False

            if self.addedRoll in (2, 3, 12):
                self.loser = True
                return  # This is the loss condition for the first roll of a craps game

            elif self.addedRoll in (7, 11):
                self.winner = True
                return  # This is the win condition for the first roll of a craps game

        else:
            self.addedRoll = self.die1.roll() + self.die2.roll()
            self.rollsCount += 1

            while True:
                if self.addedRoll == 7:
                    self.loser = True
                    return  # This is the loss condition for later rolls in a craps game
                elif self.addedRoll == self.firstRoll:
                    self.winner = True
                    return  # This is the win condition for later rolls in a craps game
                else:
                    return


def playOneGame():
    """Allows a player to play an automated game of craps in the shell."""
    player = Player()
    while True:
        player.rollDice()
        if player.winner:
            print('You win in', player.rollsCount, 'turns!')
            print('Your first roll was', player.firstRoll)
            print('Your last roll was', player.addedRoll)
            break
        elif player.loser:
            print('You lose in', player.rollsCount, 'turns!')
            print('Your first roll was', player.firstRoll)
            print('Your last roll was', player.addedRoll)
            break
