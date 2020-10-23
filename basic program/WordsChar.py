sent = input("enter the sentence: ")
count = len(sent.split())
print("Numbers of words in sentence: ",count)
for i in sent.split():
    print("Number of the characters in (",i,") is: ",len(i))