# The file class_grades.txt contains the percentage grade for each student in the class. Your job is to write a Python program that associates a percentage grade from the class_grades.txt file with a letter grade.

# For example, if class_grades.txt has the percentage grades 87, 97, 74, 86, 88 then your program should print out:
# The A(s) are [97]
# The B(s) are [87,86,88]
# The C(s) are [74]
# The D(s) are []
# The F(s) are []

grades = open("class_grades.txt")
grade_list = grades.readlines()
grades.close

def letter_grade(class_grades):

	# class_grades = map(int,class_grades)
	class_grades = [int(x) for x in class_grades] # List Comprehension

	a_grade = []
	b_grade = []
	c_grade = []
	d_grade = []
	f_grade = []

	for i in class_grades:
		if i >= 95:
			a_grade.append(i)
		elif i >= 86 and i <= 94:
			b_grade.append(i)
		elif i >= 76 and i <= 84:
			c_grade.append(i)
		elif i >= 70 and i <= 75:
			d_grade.append(i)
		else:
			i <= 69:
			f_grade.append(i)

	print "The A(s) are %r"  % (a_grade)
	print "The B(s) are %r"  % (b_grade)
	print "The C(s) are %r"  % (c_grade)
	print "The D(s) are %r"  % (d_grade)
	print "The F(s) are %r"  % (f_grade)

letter_grade(grade_list)
	
	

