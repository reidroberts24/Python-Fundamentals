class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        
    def walk(self):
        self.pet.play()
        print(f"{self.first_name} is taking {self.pet.name} for a walk.")
        return self

    def feed(self):
        self.pet.eat()
        print(f"{self.first_name} is feeding {self.pet.name}.")
        return self
    
    def bathe(self):
        self.pet.noise()
        print(f"{self.first_name} is giving {self.pet.name} a bath.")
        return self
    