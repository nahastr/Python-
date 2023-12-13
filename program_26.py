def score(stu):
	return stu[1]
student = [("swalih",88), ("nahas",55), ("swetha", 100)]
                 
print(student.sort(reverse = True, key = score(student)))
