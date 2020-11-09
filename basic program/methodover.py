class a:
    def __init__(self):
        self.val="A is runing"
    def show(self):
        print(self.val)
class b(a):
    def __init__(self):
        self.val="B is runing"
    def show(self):
        print(self.val)
a1=a()
b1=b()
a1.show()
b1.show()
