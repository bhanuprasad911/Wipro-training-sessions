class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit of {amount} successful to account {self.account_number}. Total balance is {self.balance}")
        else:
            print("Amount must be greater than zero")
    def withdraw(self, amount):
        if amount>self.balance:
            print(f"Insufficient balance in the account")
        else:
            self.balance-=amount
            print(f"Withdrawal of {amount} successful from account {self.account_number}. Total balance is {self.balance}")
    def display_balance(self):
        print(f"Account {self.account_number} has balance {self.balance}")
    def __del__(self):
        print(f"Bank account {self.account_number} is closed.")
        
Acc1 = BankAccount(123456, 1000)
Acc1.display_balance()
Acc1.deposit(500)
Acc1.withdraw(200)
Acc1.display_balance()
Acc2 = BankAccount(654321)
Acc2.display_balance()
Acc2.deposit(300)
Acc2.withdraw(100)
Acc2.display_balance()

    
    
       