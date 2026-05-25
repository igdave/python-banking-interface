import datetime
class Account:
  def __init__(self,account_number,owner_name,initial_deposit):
   self.account_number=account_number
   self.owner_name=owner_name
   self.balance= initial_deposit
   self.transaction_history=[]
  
  def deposit(self,amount):
     if amount <= 0:
      print("Invalid amount")
      return None
     self.balance += float(amount)
     print (f"you have successfully deposited {amount} your new balance is {self.balance}")
     self.transaction_history.append(f" this was a sucessful transcation at {datetime.datetime.now()}")
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
        acc=Account(account_number,name,deposit)
        self.accounts[account_number]=acc
        return self.accounts

 def transfer(self,sender_account,reciever_account,amount):
  if sender_account  not in self.accounts: 
     print("Error: This account does not exist")
     return None
  if reciever_account  not in self.accounts: 
     print("Error: This account does not exist")
     return None
  sender_obj=self.accounts[sender_account]
  reciever_obj=self.accounts[reciever_account]
  if amount >self.compliance_limit:
     print("This transaction exceeds our compliance limit")
     return None
  if amount>sender_obj.balance:
     print("Insufficeint funds")
  else:
    sender_obj.withdraw(amount)
    reciever_obj.deposit(amount)
  
   
        
        
 
# 1. Initialize the bank
bank = Banksystem()

while True:
    print("\n=== WELCOME TO THE BANK SYSTEM ===")
    print("1. Open New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. View Transaction History")
    print("6. Exit")
    
    choice = input("Kindly select an option (1-6): ")

    if choice == "1":
        acc_num = input("Enter a new account number: ")
        name = input("Enter owner's name: ")
        # input() gives text, so we convert deposit to a float number
        deposit = float(input("Enter initial deposit (Min ₦1,000): "))
        bank.open_account(acc_num, name, deposit)

    elif choice == "2":
        acc_num = input("Enter account number: ")
        if acc_num not in bank.accounts:
            print("Error: Account not found.")
        else:
            amount = float(input("Enter deposit amount: "))
            # Reach inside the registry to find the profile and call deposit
            bank.accounts[acc_num].deposit(amount)

    elif choice == "3":
        acc_num = input("Enter account number: ")
        if acc_num not in bank.accounts:
            print("Error: Account not found.")
        else:
            amount = float(input("Enter withdrawal amount: "))
            bank.accounts[acc_num].withdraw(amount)

    elif choice == "4":
        sender = input("Enter sender account number: ")
        receiver = input("Enter receiver account number: ")
        amount = float(input("Enter transfer amount: "))
        # Call the transfer function you built directly on the bank
        bank.transfer(sender, receiver, amount)

    elif choice == "5":
        acc_num = input("Enter account number: ")
        if acc_num not in bank.accounts:
            print("Error: Account not found.")
        else:
            print(f"\n--- History for {bank.accounts[acc_num].owner_name} ---")
            # Loop through the list inside the profile
            for transaction in bank.accounts[acc_num].transaction_history:
                print(transaction)

    elif choice == "6":
        print("Thank you for banking with us. Goodbye!")
        break # This stops the while loop completely

    else:
        print("Invalid choice. Please select a number between 1 and 6.")


