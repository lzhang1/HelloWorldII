# Listing_23-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rolling two 6-sided dice 1,000 times

import random

# totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(1000):
#     die_1 = random.randint(1, 6)
#     die_2 = random.randint(1, 6)
#     dice_total = die_1 + die_2
#     totals[dice_total] += 1
#
# for i in range (2, 13):
#     print "total", i, "came up", totals[i], "times"

# sides = []
# for i in range(20):
#     side_choice = random.randint(0,1)
#     sides.append(side_choice)
#     sum = 0
#     if i > 1:
#         for item in range(i-2, i+1):
#             sum += sides[item]
#         if sum == 0:
#             print "found 3(0) from index: %d"%(i-2)
#         if sum == 3:
#             print "found 3(1) from index: %d"%(i-2)
#
#
# print sides

sides = ['Header','Tails']
side_count = 0
for i in range(100):
    side_choice = random.choice(sides)
    if side_choice == 'Header':
        side_count += 1
    else:
        side_count = 0
    print side_choice,
    if side_count > 3:
        print "from No %d"%(i-side_count+1)
        break
