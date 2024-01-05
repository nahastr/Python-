def is_palindrome(n):
	if(n == n[::-1]):
		print("Its palindrome")
	else:
		print("Its not a palindrome")	
	


word = input("Enter the word ")
is_palindrome(word)
