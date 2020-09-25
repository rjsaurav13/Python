# -*- coding: utf-8 -*-
"""


@author: saurav
"""

cityname = [] 
for i in range(0,5):
    city=input()
    cityname.append(city)
print(cityname)  
srch = input()
for i in range(0,5):
    
    if srch==cityname[i]:
        print("found element at position:",i+1)
    else:
        print("Element not found")
    