low = int(input("Enter the lower limit :"))
up = int(input("Enter the upper limit :"))

for i in range(low, up + 1):
	if i > 1:
		flag = 0
		for j in range(2, i):
			if (i%j==0) :
				flag = 1
				break
			
		if flag == 0:
			print(i)
