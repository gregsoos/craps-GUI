"""
File: crapsGUI.py
Author: Greg Soos
Last modified: 3/24/2023

Pops up a window that allows the user to play the game of craps.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from craps import Player


class CrapsGUI(EasyFrame):

    def __init__(self):
        """Initializes GUI window, including size, if resizable, labels, and buttons."""
        EasyFrame.__init__(self, title='Craps')
        self.setSize(500, 400)
        self.setResizable(False)  # Creating GUI as a static size.
        self.play = Player()
        self.dieImageLabel1 = self.addLabel('', row=0, column=0, sticky='NSEW')
        self.dieImageLabel2 = self.addLabel('', row=0, column=1, sticky='NSEW', columnspan=2)
        self.dieImage1 = self.dieImage2 = PhotoImage()
        self.outputArea = self.addTextArea("", row=1, column=0, columnspan=2, wrap='char')  # Adds scroll bar to text.
        self.addButton(row=2, column=0, text='Roll', command=self.nextRoll)
        self.addButton(text='New game', row=2, column=1, command=self.newGame)
        self.refreshImages()

    def nextRoll(self):
        """Roll dice. Print sum of dice values, and tell player they won/lost if appropriate."""
        self.play.rollDice()
        self.outputArea.appendText('Total = ' + str(self.play) + '\n')
        self.refreshImages()

        if self.play.loser:
            self.outputArea.appendText('You lose in ' + str(self.play.rollsCount) + ' rolls!' + '\n')
            self.play = Player()

        elif self.play.winner:
            self.outputArea.appendText('You win in ' + str(self.play.rollsCount) + ' rolls!' + '\n')
            self.play = Player()

    def newGame(self):
        """Begin a new game. Resets play history and dice images."""
        self.play = Player()
        self.outputArea.setText("")
        self.refreshImages()

    def refreshImages(self):
        """Set dice images in GUI."""
        fileName1 = 'DICE/' + str(self.play.die1) + '.gif'
        fileName2 = 'DICE/' + str(self.play.die2) + '.gif'
        self.dieImage1 = PhotoImage(file=fileName1)
        self.dieImage2 = PhotoImage(file=fileName2)
        self.dieImageLabel1['image'] = self.dieImage1
        self.dieImageLabel2['image'] = self.dieImage2


def main():
    """Create GUI."""
    CrapsGUI().mainloop()


if __name__ == '__main__':
    main()
