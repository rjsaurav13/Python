# -*- coding: utf-8 -*-
"""


@author: saurav
"""

python=open('ab.txt','w')
python.write("hello world")

python.close()
python = open("ab.txt", "r")
print(python.read())