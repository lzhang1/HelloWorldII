# Listing_11-7.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# program to figure out combinations of hot dog ingredients
# including total calories for each

# Calories for each part of the hot dog
letters = ['b','c']
letters.append('d')
letters.insert(0,'a')
letters.insert(0,'i')
letters.extend(['e','f','g'])
print letters
letters.remove('g')
print len(letters)
print letters
del letters[len(letters)-1]
print letters
letters.pop()
print letters
letters.pop(0)
print letters
if 'a' in letters:
    print "ok"
print letters.index('a')
for i in range(len(letters)):
    print letters[i]

letters.insert(0,'e')
print letters
letters.sort()
print letters
letters.reverse()
print letters


# import easygui
# flavor = easygui.buttonbox("which one you pickup", choices=['Yes','NO','Do not know'])
# easygui.msgbox('your flavor: ' + flavor)
# flavor = easygui.choicebox("which one you pickup", choices=['Yes','NO','Do not know'])
# easygui.msgbox('your flavor: ' + flavor)

for i in range(10,0,-1):
    print i