import datetime
class Account:
  def __init__(self,account_number,owner_name,initial_deposit):
   self.account_number=account_number
   self.owner_name=owner_name
   self.balance= initial_deposit
   self.transaction_history=[]
  
  def deposit(self,amount):
     if amount<=0:
       return None
     self.balance += float(amount)
     print (f"you have successfully deposited {amount} your new balance is {self.balance}")
     return self.balance
  def withdraw(self,amount):
     if amount<=0:
       return None
     if amount > self.balance:
       print("Insufficient funds")
       self.transaction_history.append("FAILED WITHDRAWAL ATTEMPT")
       return None
     else:
       print("succesfull transacation")
       self.transaction_history.append(f" this was a sucessful transcation at {datetime.datetime.now()}")
       self.balance -= float(amount)
     print (f"you have successfully withdrawn {amount} your new balance is {self.balance}")
     return self.balance    
   
      
class Banksystem:
 def __init__(self):
  self.accounts={}
  self.compliance_limit=500000
def open_account(self, account_number, name, deposit):
        if deposit < 1000:
            print("Error: Initial deposit must be at least ₦1,000 to open an account.")
            return None
        
        # Create the account and store it in the bank dictionary
        new_account = Account(account_number, name, deposit)
        self.accounts[account_number] = new_account
        print(f"Account {account_number} successfully opened for {name}.")
        return new_account
bank=Banksystem()   
 
a1=bank.open_account(20000,"dacid",5000.00)
hi=a1.deposit(588)
h1=a1.withdraw(100)
ae=a1.transaction_history
print(ae)
