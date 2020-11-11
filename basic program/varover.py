#create a class called students create two students objects and perform addition of there marks using operator overloading
class student:
    def __init__(self,m,m1):
        self.m=m
        self.m1=m1
    def __add__(self,other):
        m=self.m+other.m
        m1=self.m1+other.m1
        s3=student(m,m1)
        return s3
s1=student(50,60)
s2=student(60,70)
s3=s1+s2
print(s3.m," ",s3.m1)

