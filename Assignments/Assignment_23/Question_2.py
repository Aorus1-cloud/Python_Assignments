class BankAccount:
    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name 
        self.Amount = amount

    def Display(self):
        print(f"Account Holder :{self.Name} ,Amount : {self.Amount}")
    
    def Deposit(self):
        deposit_amount = 0

        deposit_amount = int(input("Enter deposit amount(in $):")) 

        self.Amount += deposit_amount

        print(f"Updated Balance :{self.Amount}$")

    def Withdraw(self):
        withdraw_amount = 0

        withdraw_amount = int(input("Enter Withdrawal Amount (in $):"))

        if withdraw_amount > self.Amount :
            return print("Insufficient Balance.")
        
        self.Amount -= withdraw_amount

        print(f"Updated Balance :{self.Amount}$")

    def CalculateInterest(self):
        Interest = 0 

        Interest = (self.Amount * BankAccount.ROI) / 100

        print(f"Interest on your amount is :{Interest}$")

obj1 = BankAccount("Jayesh Patil",100)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()

obj2 = BankAccount("Jack Mathew",500)
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()

    
