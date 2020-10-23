list1=[]
list2=[]
n = int(input("enter the number: "))
print("enter the value: \n")
for i in range(n):
    temp = int(input())
    list1.append(temp)
for j in list1:
    if j not in list2:
        list2.append(j)
print("rear values are: ",list2)


