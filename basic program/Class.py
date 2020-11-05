#create a class which has init  function to display value for instance variable
class Person:
  def init(self, name):
    self.name = name
  def display(self):
    print(self.name)
name=input("Enter Name")
p1=person(name)
p1.init(name)
p1.display
