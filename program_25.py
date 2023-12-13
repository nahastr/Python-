students = { }

n = int(input("Enter the number of students"))

for i in range(n):
	Name = input("Enter the name ")
	Age = input("Enter the age ")
	Grade = input("Enter the grade ")
	
	students[Name] = Age, Grade
	
print(students)

