sen = input("Enter the string\n")
count = 0
for i in sen:
	if i == " ":
		continue
	else:
		count += 1
		
print(count)
