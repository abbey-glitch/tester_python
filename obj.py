class Dog(object):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("I speak {}".format(self.name))

class Bingo(Dog):
    def __init__(self, name, salary):
        self.salary = salary
        super(name).__init__(name)
        print("my name is{}".format(self.name))

rodger = Dog('john')
rodger.speak()
a = Bingo('jame', 400)
a.speak()
print("my name is  {}".format(rodger.name))