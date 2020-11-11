#to create a class called books demonstrate the addition of pages of two books using operator overloading
class books:
    def __init__(self, p):
        self.p = p


    def __add__(self, other):
        p = self.p + other.p

        b3 = student(p)
        return s3

b1=student(50)
b2=student(60)
b3=b1+b2
print(b3.p)
