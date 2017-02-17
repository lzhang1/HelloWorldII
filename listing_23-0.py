# Listing_23-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rolling two 6-sided dice 1,000 times

import random
from card import Card

deck =[]
for suit_id in range(1,5):
    for rank_id in range(1,14):
        deck.append(Card(suit_id, rank_id))

deck.append(Card(5,14))
deck.append(Card(6,14))


hand = []
for i in range(0,5):
    card_pickup = random.choice(deck)
    hand.append(card_pickup)
    deck.remove(card_pickup)

for i in range(0,5):
    print hand[i].shortname,




