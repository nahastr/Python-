def factorial(n):
	if(n < 1):
		return 1
	else:	
		return n*factorial(n-1)


fact = int(input("Enter the number "))
print("factorial of", fact, "is", factorial(fact))
