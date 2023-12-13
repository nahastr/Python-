num = int(input("Enter the number "))
names = []

for i in range(num):
	names.append(input("Enter the name "))
	
names.sort()


for i in names:
	print(i)
