## Copy BankAccount class from previous assignment
class BankAccount:
    accounts = [] #holds all account instances

    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.interest_rate = int_rate
        BankAccount.accounts.append(self) #adds the new Account instance to the list of accounts

    def deposit(self, amount):
        self.balance += amount
        print(f"You have added ${amount} to your account. Your balance is now ${self.balance}")
        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"You do not have sufficient funds. Your balance is ${self.balance}.")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount}. Your balance is now ${self.balance}.")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}\nInterest Rate: {self.interest_rate*100}%")
        return self
    
    def yield_interest(self):
        new_balance = self.balance * self.interest_rate
        self.balance += round(new_balance, 2)
        print(f"You earned ${round(new_balance,2)} from interest. You now have a total balance of ${self.balance}")
        return self
    
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [] #empty list to hold all active user accounts
        self.add_account() #call add_account() method upon a new user instantiation

    def add_account(self):
        account = BankAccount(int_rate=0.02, balance=0) #create new default account when user decides to add an account
        self.accounts.append(account) #add new account to the list of user's acounts
        return self
    
    def make_deposit(self, acct_index, amount):
        if 0 <= acct_index and acct_index < len(self.accounts): #check that the given index is valid
            self.accounts[acct_index].deposit(amount)  #deposit amount from account at given index
        else:
            print("Invalid account index.")
        return self
    
    def make_withdrawal(self, acct_index, amount):
        if 0 <= acct_index < len(self.accounts): #check that the given index is valid
            self.accounts[acct_index].withdraw(amount) #withdraw amount from account at given index
        else:
            print("Invalid account index.")
        return self
    
    def display_user_balance(self, acct_index):
        if 0 <= acct_index < len(self.accounts): #check that the given index is valid
            self.accounts[acct_index].display_account_info() #display account info at given index
        else:
            print("Invalid account index.")
        return self
    
    def transfer_money(self, amount, other_user): 
        self.make_withdrawal(0,amount)
        print(f"${amount} successfully withdrawn from {self.name}'s primary account.")  # withdrawing into account at first index
        other_user.make_deposit(0,amount)
        print(f"${amount} successfully deposited into {other_user.name}'s primary account.") # depositing into account at first index
        print("Transaction completed successfully.")
        return self

user1 = User("Reid", "rrob@gmail.com")
user1.make_deposit(0,1000)

user2 = User("Blake", "bbob@gmail.com")
user1.transfer_money(600, user2)
