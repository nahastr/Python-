class account:
	def __init__(self):
		print("_____BANK ACCOUNT_____")
		self.balance = 0
		
	def deposit(self):
		amount = int(input("Enter the amount : "))
		self.balance += amount
		print(amount," deposited Current balance is ", self.balance) 
		
	def withdraw(self):
		amount = int(input("Enter the amount to be withdrawn: "))
		if amount > self.balance :
			print("insufficient balance\nPlease enter a valid amount")
		else:
			self.balance -= amount
			print(amount," withdrawn from your account")
			
	def display(self):
		print("Current balance is ",self.balance)
		
		
myaccount = account()

myaccount.deposit()
myaccount.withdraw()
myaccount.display()
	
 
		
