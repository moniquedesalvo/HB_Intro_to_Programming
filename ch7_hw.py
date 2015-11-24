def find_average(num1, num2, num3):
	if num1 == str and num2 == str and num3 == str:
		return (num1 + num2 + num3)/3
	else:
		return "Sorry, the input(s) are invalid."


print find_average("5", 2, 3)

my_file = open("my_text.txt")
my_file.readline()
print my_file.readline()
