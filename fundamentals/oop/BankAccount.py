class Account:
    accounts = [] #holds all account instances

    def __init__(self, interest_rate, initial_balance=0):
        self.balance = initial_balance
        self.interest_rate = interest_rate / 100
        Account.accounts.append(self) #adds the new Account instance to the list of accounts

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
    
    @classmethod
    def print_all_accounts_info(cls):
        current_acct = 1
        for acct in cls.accounts:
            print(f"############################# Account {current_acct} #############################")
            acct.display_account_info()
            current_acct += 1
            


acct1 = Account(3.25, 8000)
acct1.deposit(500).deposit(85).deposit(631).withdraw(2450).yield_interest().display_account_info()

acct2 = Account(1.5, 20000)
acct2.deposit(2400).deposit(745).withdraw(5000).withdraw(2000).withdraw(2000).withdraw(10000).yield_interest().display_account_info()

Account.print_all_accounts_info()
