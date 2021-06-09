class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
      
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if(self.balance - amount > 0):
            self.balance -= amount
            return self
        else:
            print("Insuficient Funds: deducting $5")
            self.balance -= 5
        return self
      
    def display_account_info(self):
        print(self.balance)
        return self
        

    def yield_interest(self):
        if(self.balance > 0):
            self.balance = self.balance * self.int_rate
        return self
    
class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account
    
    def make_deposit(self, amount, index):
        self.account[index].balance += amount
        print(f"{self.name} added {amount} to account {index + 1}")
        return self
    
    def make_withdrawl(self,amount, index):
        self.account[index].withdraw(amount)
        print(f"{self.name} withdrew {amount}.")
        return self
        
    def display_user_balance(self, index):
        print(f"{self.name}'s account {index + 1} balance is {self.account[index].balance}")
        return self

Tim_Accounts = [BankAccount(0.02, 0), BankAccount(0.02, 0)]      
User_Tim = User("Tim", "Tim123@gmail.com", Tim_Accounts)

User_Tim.make_deposit(200,0).make_withdrawl(100,0).display_user_balance(0)
User_Tim.make_deposit(200,1).make_withdrawl(100,1).display_user_balance(1)



        