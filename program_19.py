s = input("Enter the string\n")
first_char = s[0]
last_char = s[-1]

new_string = last_char + s[1:-1] + first_char
print(new_string)
