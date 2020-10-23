py = open("lm.txt","r")
py2 = open("no.txt","w")
for i in py:
    py2.write(i)
py.close()
py2.close()

