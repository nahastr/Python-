class Rect:
	def __init__ (self, length, breadth):
		self.length = length
		self.breadth = breadth
		
	def area(self):
		return self.length * self. breadth
		
	def perimeter(self):
		return 2*(self.length + self.breadth)
		

length = int(input("Enter the length "))
breadth = int(input("Enter the breadth "))

rectangle = Rect(length, breadth)

print("Area : ",rectangle.area())
print("Perimeter : ",rectangle.perimeter())

