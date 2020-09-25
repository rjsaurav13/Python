# -*- coding: utf-8 -*-
"""


@author: saurav
"""


even = [] 
odd = []
len = int(input())
for i in range(0,len):
    num=int(input())
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)    
print("Even list :",even)
print("Odd list :",odd)