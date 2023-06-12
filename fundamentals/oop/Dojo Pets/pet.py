class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        return self


######## dog sub-class
class Dog(Pet):
    def noise(self):
        print("woof woof")
        return self

    
    def feed(self):
        print("The puppy ate his food.")
        return self

######## cat sub-class
class Cat(Pet):
    def noise(self):
        print("meow")
        return self
    
    def feed(self):
        print("The cat pounced on her prey.")
        return self