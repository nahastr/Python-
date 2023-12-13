def palindrome(s):
	return s==s[::-1]
	
s = input("Enter the text : ")

if(palindrome(s)):
	print("its is a palindrome")
else:
	print("its not a palindrome")
