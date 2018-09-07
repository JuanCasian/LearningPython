class myClass():
    def method1(self):
        print("Hello my friend")

    def method2(self, mystr):
        print("Hello my dearest frined: " + mystr)

class additionClass(myClass):
    value = 0;
    def add(self, *nums):
        for num in nums:
            self.value =  self.value + num;
    def print_value(self):
        print("Your value is: " + str(self.value))

class1 = myClass()
class2 = additionClass()

class1.method1();
class2.method2("Juan")
class2.print_value()
class2.add(5, 5)
class2.print_value()
