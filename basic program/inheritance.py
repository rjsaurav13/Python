class a:
    def feature(self):
        print("feature 1 is working")
    def feature1(self):
        print("feature 2 is working")
class b(a):
    def feature2(self):
        print("feature 3 is working")
    def feature3(self):
        print("feature 4 is working")
b1=b()
b1.feature()
b1.feature1()
b1.feature2()
b1.feature3()
