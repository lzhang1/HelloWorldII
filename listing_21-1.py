# Listing_21-1.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# A program to print squares and cubes
print "Result\\nDetail"
print 'Result\\nDetail'
print "Number "+"\tSquare "+"\tCube"
for i in range (1, 11):
    print i, '\t', i**2, '\t', i**3

number = 12.6
print "Number: %i"%number
print "Number: %d"%int(number)
number = '%.2f'%number
print "Number: "+number
name = "ray"
old = 12
print "My name is {0:s}, I am {1:d} years old".format(name, old)
name_string = 'Sam,Brad,Alex,Cameron,Toby,Gwen,Jenn,Connor'
name_list = name_string.split(',')
for i in range(len(name_list)):
    print 'NO {0:d} is {1:s}'.format(i, name_list[i])

name_str = ':'.join(name_list)
print name_str


for i in range(1,8):
    print 'num: %.2f'%(i/8.0)
