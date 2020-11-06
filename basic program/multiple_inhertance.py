class a:
    def feature(self):
        print("feature 1 is working")
    def feature1(self):
        print("feature 2 is working")
class b:
    def feature2(self):
        print("feature 3 is working")
    def feature3(self):
        print("feature 4 is working")
class c(a,b):
    def feature4(self):
        print("feature 5 is working")
c1=c()
c1.feature()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
