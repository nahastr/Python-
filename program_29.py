x = lambda a, b : a * b
p = lambda a, b : 2*(a + b)

length = int(input("Enter the length of rectange : "))
breadth = int(input("Enter the breadth of rectange : "))

print("Area ", x(length, breadth))
print("Perimeter ", p(length, breadth))
