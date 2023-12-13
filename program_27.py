thedict = {}
l = []

n = int(input("enter the number of words " ))

for i in range(n):
	name = input("Enter the name ")
	age = input("Enter the age ")
	
	thedict[name] = age
	
l = list(thedict.items())

l.sort()
print("Printing in ascending order \n", l)

l.sort(reverse = True)
print("Printing in descending order \n", l)

thedict = dict(l)

print(thedict)

