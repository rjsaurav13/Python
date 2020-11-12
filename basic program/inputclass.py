# create a class person with user input
class person:
    def __init__(self):
        self.firstname=input("Enter first name: ")
        self.lastname=input("Enter last name: ")
    def show(self):
        print(self.firstname,self.lastname)
p1=person()
p1.show()