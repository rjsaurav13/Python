class person:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def greet(self):
        print("Hello" ,self.name , "from" ,self.place)

n=input("Enter name ")
p=input("Enter place ")

p1 = person(n,p)
p1.greet()
