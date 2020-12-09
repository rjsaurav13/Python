len=int(input())
for i in range(2,len):
    for x in range(2,i):
        if(i%x==0):
            break
    else:
        print(i,end=",")


