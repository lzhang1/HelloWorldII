# Listing_23-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rolling two 6-sided dice 1,000 times

import random

class Card:
    def __init__(self, suit_id, rank_id):
        self.suit_id = suit_id
        self.rank_id = rank_id

        if self.rank_id == 1:
            self.rank = "Ace"
            self.value = 1
        elif self.rank_id == 11:
            self.rank = "Jack"
            self.value = 10
        elif self.rank_id == 12:
            self.rank = "Queen"
            self.value = 10
        elif self.rank_id == 13:
            self.rank = "King"
            self.value = 10
        elif self.rank_id > 1 and self.rank_id < 11:
            self.rank = str(self.rank_id)
            self.value = 1
        elif self.rank_id == 14:
            self.rank = "Joker"
            self.value = 11
        else:
            self.rank = "RankError"
            self.value = -1

        if self.suit_id == 1:
            self.suit = "Diamonds"
        elif self.suit_id == 2:
            self.suit = "Hearts"
        elif self.suit_id == 3:
            self.suit = "Spades"
        elif self.suit_id == 4:
            self.suit = "Clubs"
        elif self.suit_id == 5:
            self.suit = "Black"
        elif self.suit_id == 6:
            self.suit = "Color"
        else:
            self.suit = "SuitError"

        if self.value == 10:
            self.shortname = self.suit[0] + self.rank[0]
        elif self.value == 11:
            self.shortname = self.suit[0] + self.rank
        else:
            self.shortname = self.suit[0] + self.rank[0]

if __name__ == "__main__":
    deck = []
    for suit_id in range(1,5):
        for rank_id in range(1,14):
            deck.append(Card(suit_id, rank_id))

    deck.append(Card(5,14))
    deck.append(Card(6,14))
    for i in range(1,55):
        print deck[i].shortname