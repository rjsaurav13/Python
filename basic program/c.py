#create a class person with name and age as instence variable and initialize them using init function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Hello my name is "+ self.name,"and i am ",self.age,"years old")



p1 = Person("saurav", 20)
p1.show()