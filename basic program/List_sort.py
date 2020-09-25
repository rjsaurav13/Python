# -*- coding: utf-8 -*-
"""


@author: saurav
"""

list = [] 
for i in range(0,5):
    num=int(input())
    list.append(num)
list.sort()  
print(list)
print("Second largest number: ",list[-2])
print("second smallest number: ", list[1])