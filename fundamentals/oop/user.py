class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    
    def display_info(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nIs Rewards Member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")
        return self
    
    def enroll(self):
        if self.is_rewards_member == True:
            print(f"{self.first_name} is already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"{self.first_name} is now a member and has been awarded {self.gold_card_points} gold card points.")
            return self
    
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"Not enough gold card points. {self.first_name} currently has {self.gold_card_points} points.")
            return False
        else:
            self.gold_card_points -= amount
            print(f"{self.first_name} spent {amount} points. {self.first_name} now has {self.gold_card_points} gold card points remaining.")
            return self
        

user1 = User("Michael", "Jordan", "mj@gmail.com", 48)
user1.enroll().spend_points(50).display_info().enroll()

user2 = User("Alex", "Bregman", "goat@gmail.com", 27)
user2.enroll().spend_points(80).display_info()

user3 = User("Erling", "Haaland", "strikerone@gmail.com", 28)
user3.display_info().spend_points(40)