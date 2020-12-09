f1 = open("g.txt","r")
f2 = open("g1.txt","w")
for i in f1:
    f2.write(i)
f1.close()
f2.close()