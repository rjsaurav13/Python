# -*- coding: utf-8 -*-
"""


@author: saurav
"""

rows = int(input("Please Enter the total Number of Rows  : "))

i = rows
while(i > 0):
    j = i
    while(j > 0):      
        print( j, end = '  ')
        j = j - 1
    i = i - 1
    print()