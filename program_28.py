student=[]
n = int(input("Enter the number of students"))
days = int(input("Enter the total no of days "))

for i in range(n):
	name = input("Enter the name ")
	attendance = int(input("Enter the no of present days "))
	
	per = (attendance / days) * 100
	student.append((name, per))
	
	
student.sort(reverse = True, key = lambda x: x[1])
print(student) 

