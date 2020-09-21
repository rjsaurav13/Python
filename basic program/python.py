# -*- coding: utf-8 -*-
"""


@author: saurav
"""
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = int(input())
fact=factorial(num)
print("factorial = ",fact)