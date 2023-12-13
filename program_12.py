def binary_to_decimal(n):
	decimal = 0
	power = 1
	while(n > 0):
		rem = n % 10
		n = n//10
		decimal += rem * power
		power = power * 2
	return decimal

binary = int(input("enter the binary number "))
print(binary_to_decimal(binary))
