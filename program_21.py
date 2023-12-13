n = int(input("enter the number of elements : "))
words=[]
max = 0;

for i in range(n):
	words.append(input("Enter the word "))
	if len(words[i]) > max:
		max = len(words[i])
		word = words[i]
	
print("longest word is", word, "with the length of ", max)
