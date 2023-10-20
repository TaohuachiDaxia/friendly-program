class Animal:
    def __init__(self,name):
        self.name=name
        
    def move(self):
        print("Let's run now!")
        
    def show_info(self):
        return "Animal name is {0}".format(self.name)
        
class Cat(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
        
cat1=Cat("Tommy", 5)
    
print("Cat name is: {0}; cat age is: {1}".format(cat1.name,cat1.age))
cat1.move()
print(cat1.show_info())