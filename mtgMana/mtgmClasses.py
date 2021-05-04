#! python3

from random import randint

class Deck:
    def __init__(self, good_lands, lands, total):
        self.lands = lands
        self.good_lands = good_lands
        self.total = total

    def draw_card(self):
        x = randint(1, self.total)
        if x <= self.good_lands:
            self.good_lands -= 1
            self.lands -= 1
            self.total -= 1
            return 1
        elif x <= self.lands:
            self.lands -= 1
            self.total -= 1
            return 2
        else:
            self.total -= 1
            return 3

    def draw_hand(self):
        cards = 0
        lands = 0
        pip_lands = 0
        for i in range(7):
            card_type = self.draw_card()
            cards += 1
            if card_type < 3:
                lands += 1
                if card_type == 1:
                    pip_lands +=1
        return [cards, lands, pip_lands]

    def start_game(self):
        mulls = 0
        while True:
            hand = self.draw_hand()
            if 1 < hand[1] < 6:
                break
            if mulls == 3:
                break
            mulls += 1
        hand[0] = hand[0] - mulls
        return hand

    def draw_to_turn(self, casting_turn):
        hand = self.start_game()
        turn = 2
        if casting_turn < 2:
            return hand
        while turn <= casting_turn:
            card_type = self.draw_card()
            hand[0] += 1
            if card_type < 3:
                hand[1] += 1
                if card_type == 1:
                    hand[2] += 1
            turn += 1
        return hand
