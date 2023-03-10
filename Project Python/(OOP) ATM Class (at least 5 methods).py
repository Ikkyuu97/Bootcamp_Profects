class ATM:
    def __init__(self, names, balance: float, password: str):
        self.names = names
        self.balance = balance
        self.password = password
        
    def check_balance(self):
        message = f"Account: {self.names}, Balance: {self.balance} THB."
        print(message,"\n")
    def deposit(self, money: float):
        self.balance += money
        print(f"Deposit Amount of {money} THB.")
        print(f"New Balance: {self.balance} THB.")
        print("Deposit successfully.\n")
    def withdraw(self,money: float):
        self.balance-=money
        print(f"Withdrawal of {money} THB.")
        print(f"New Balance: {self.balance} THB.")
        print("Withdraw successfully.\n")
    def transfer(self,money: float,payee: str):
        self.balance-=money
        print(f"Transter to {payee}, {money} THB.")
        print(f"New Balance: {self.balance} THB.\n")
    def paybill(self,money: float,payee: str,fee: float):
        self.balance=self.balance-money-fee
        print(f"Paybill to {payee}, {money+fee} THB.")
        print(f"New Balance: {self.balance} THB.\n")
    def change_name(self, new_acc_name: str):
        self.names = new_acc_name
        print(f"New Name: {self.names}")
        print("Your account name has been changed.\n")
    def change_password(self, new_password: str):
        self.password = new_password
        print(f"New Password: {self.password}\nYour password has been changed.")
        
#Set constant value
customers = []
deposit_value = 0
withdraw_value = 0
transfer_value = 0
paybill_value = 0

#Input data
customers.append(input("Your name: "))
customers.append(float(input("Balance: ")))
customers.append(input("Your password: "))
bbl = ATM(customers[0],customers[1],customers[2])

#Check Balance
bbl.check_balance()

#Deposit
dep = input("Do you want to deposit?(y/n): ").lower()
if dep=='y':
    deposit_value = float(input("Deposit Amount: "))
    bbl.deposit(deposit_value)
else:pass

#Withdraw
withdr = input("Do you want to withdraw?(y/n): ").lower()
if withdr=='y':
    withdraw_value = float(input("Withdraw Amount: "))
    if withdraw_value<=100:
        print("Minimum withdraw is 100 THB., Please Try again")
        withdraw_value = float(input("Withdraw Amount: "))
    if withdraw_value > (customers[1]+deposit_value):
        print("Balance is not enough, please Try again")
        withdraw_value = float(input("Withdraw Amount: "))    
    else:bbl.withdraw(withdraw_value)
else:pass

#Transfer
transf = input("Do you want to transfer?(y/n): ").lower()
if transf=='y':
    transfer_value = float(input("Transfer Amount: "))
    payee_name = (input("Transfer to: "))
    if transfer_value > (customers[1]+deposit_value-withdraw_value):
        print("Balance is not enough, please Try again")
        transfer_value = float(input("Transfer Amount: "))
    else:bbl.transfer(transfer_value,payee_name)
else:pass

#Paybill
paybill = input("Do you want to paybill?(y/n): ").lower()
if paybill=='y':
    paybill_value = float(input("Paybill Amount: "))
    payee_bill_name = (input("Payee: "))
    fee_value = float(input("Fee Amount: "))
    if paybill_value > (customers[1]+deposit_value-withdraw_value-transfer_value):print("Balance is not enough, please Try again later.")
    else:bbl.paybill(paybill_value,payee_bill_name,fee_value)
else:pass

#New Name
changename = input("Do you want to change your name?(y/n): ").lower()
if changename=='y':bbl.change_name(input("Do you want to change your name as: "))
else:pass

#New password
changepw = input("Do you want to change your password?(y/n): ").lower()
if changepw=='y':
    len_pw = 6
    while len_pw == 6:
        new_pw=input("Please enter 6 digits[0-9]: ")
        if len(new_pw)==len_pw:
            bbl.change_password(new_pw)
            break
        else:
            print("Invalid password!")
