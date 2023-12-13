def add(num1, num2):
	return num1 + num2
def sub(num1, num2):
	return num1 - num2
def mul(num1, num2):
	return num1 * num2
def div(num1, num2):
	return num1 / num2
def pow(num1, num2):
	return num1 ** num2
	
def cal(num1,num2,oper):
	if oper == 1:
		print(add(num1,num2))
	elif oper == 2:
		print(sub(num1,num2))
	elif oper == 3:
		print(mul(num1,num2))
	elif oper == 4:
		print(div(num1,num2))
	elif oper == 5:
		print(pow(num1,num2))
	else:
		print("invalid choice")	

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
print("1.Addition \n2.Subtract \n3.multply \n4.division \n5.Power")
oper = int(input("Select the operation "))

cal(num1, num2, oper)	
