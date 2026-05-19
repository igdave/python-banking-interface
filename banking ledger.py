import datetime

class Account:
    def __init__(self, account_number, owner_name, initial_deposit):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = float(initial_deposit)
        self.transaction_history = []
  
    def deposit(self, amount):
        if amount <= 0:
            return None
        self.balance += float(amount)
        print(f"you have successfully deposited {amount} your new balance is {self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            return None
        if amount > self.balance:
            print("Insufficient funds")
            self.transaction_history.append("FAILED WITHDRAWAL ATTEMPT")
            return None
        else:
            print("succesfull transacation")
            self.transaction_history.append(f" this was a sucessful transcation at {datetime.datetime.now()}")
            self.balance -= float(amount)
        print(f"you have successfully withdrawn {amount} your new balance is {self.balance}")
        return self.balance    


# --- Running Your Code ---
# Creating one single account directly from your class
a1 = Account(20000, "david", 5000.00)

hi = a1.deposit(588)
h1 = a1.withdraw(100)

ae = a1.transaction_history
print(ae)
