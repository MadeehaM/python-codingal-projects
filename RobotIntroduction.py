class Robots:

    def __init__(self,name):
        self.name = name

    def intro(self):
        print("Hi there, my name is", self.name)

ob=Robots('Tom')
ob2=Robots('Jerry')

ob.intro()
ob2.intro()
