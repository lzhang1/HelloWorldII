# Listing_22-5.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Using write mode on an existing file

the_file = open('notes.txt', 'w')
the_file.write("Wake up\n")
the_file.writelines("Watch cartoons\n")
the_file.writelines("Byebye")
the_file.close()

file = open("notes.txt","r")
for line in file.readlines():
    print line

file.close()
