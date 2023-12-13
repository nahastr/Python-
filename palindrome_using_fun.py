def palin(n):
	rev = 0
	rem = 0
	while(n > 0):
		rem = n % 10
		rev = rev * 10 + rem
		n = n // 10
	return rev	


num = int(input("Enter the number :"))
if(palin(num) == num):
	print("Its palindrome")
else:
	print("its not a palindrome")
