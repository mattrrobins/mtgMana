README for mtgMana.py

This is a small program for running probabilities for casting cards on curve
in the Magic: The Gathering card game.  

The idea of this program follows from Frank Karsten's excellent article found
here: https://strategy.channelfireball.com/all-strategy/mtg/channelmagic-articles/how-many-colored-mana-sources-do-you-need-to-consistently-cast-your-spells-a-guilds-of-ravnica-update/

Frank's tables were given for a rule that has since been updated, and so aren't as
accurate as they once were.  This is because Vancouver mulligan is no longer in effect, and we use the London mulligan here, i.e.,

London Mulligan Rules:
-Initial draw 7 cards.
-Decide to mulligan or not.
-If mulligan:
-Shuffle the hand back in the deck and draw a new 7 card hand.
-Decide to mulligan or not.
-If not:
-Put 1 on the bottom of the deck, and begin the game with 6 cards.
-If mulligan:
-Shuffle the hand back in the deck and draw a new 7 card hand.
-Decide to mulligan or not.
-If not:
-Put 2 on the bottom of the deck, and begin the game with 5 cards.
-If mulligan:
-Shuffle the hand back in the deck and draw a new 7 card hand.
-Decide to mulligan or not:
-If not:
-Put 3 on the bottom of the deck, and begin the game with 4 cards.
-Mulliganning again is ignored, since if we mulligan again the odds of winning are so slim, so the odds casting a card on curve are irrelevant.

I've updated the methodology using the above definitions of the London mulligan, and translated the program from Java to Python.



To Install:
- Create a directory mtgDir, cd into there
- Using your favorite virtual environment, create a new one, e.g., venv
  in the new directory mtgDir
- git clone https://github.com/mattrrobins/mtgMana.git
- cd mtgMana
- pip install -r requirements.txt

To Run:
cd ~/mtgDir/mtgMana
python mtgMana

To Configure:
In __main__.py, there are 5 variables to to modify the probabilities:

These depend on the card you have in mind to run a probability analysis on
the odds of casting the card on curve.

-TOTAL - The total number of cards in your starting deck.
-LANDS - The total number of lands in your starting deck.
-GOOD_LANDS - The total number of lands producing the color of mana of needed.
-CASTING_TURN - The turn (i.e., the CMC) you wish to cast the card.
CASTING_PIPS - The number (up to multiplicity) of colors needed to cast the desired card.

Examples:
Ex1:
You wish to cast Wrath of God (see https://scryfall.com/card/2xm/39/wrath-of-god).
This has a CMC of 4 (i.e., would like to cast on turn 4) with two white pips.
Suppose we have a standard constructed deck of 60 total cards, 26 total lands, and 16 lands which produce white mana on curve.
Then we have a configuration of the following

TOTAL = 60
LANDS = 26
GOOD_LANDS = 16
CASTING_TURN = 4
CASTING_PIPS = 2

This yields a probability of 92.39% chance of casting Wrath of God on curve.
