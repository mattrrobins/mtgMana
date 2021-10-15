#! python3

# mtgMana program for calculating probabilities for deck construction.

from mtgmFunctions import *
from mtgmClasses import *

# Preamble

TOTAL = 60
LANDS = 24
GOOD_LANDS = 11
CASTING_TURN = 3
CASTING_PIPS = 1

# Begin program loop

# Begin program
if __name__ == '__main__':
    count_OK = 0
    count_conditional = 0
    for i in range(1000000):
        deck = Deck(GOOD_LANDS, LANDS, TOTAL)
        hand = deck.draw_to_turn(CASTING_TURN)
        if hand[1] >= CASTING_TURN:
            count_conditional += 1
            if hand[2] >= CASTING_PIPS:
                count_OK += 1

    percent = truncate(count_OK / count_conditional, 4) * 100
    print(f'You have a {percent}% chance of casting your card on curve.')
