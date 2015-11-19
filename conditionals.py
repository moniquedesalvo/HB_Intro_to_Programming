import datetime

#1. Use the python interpreter to find out if the following boolean expressions are True. If they are False, how would you fix them to make them True?

# if 8 == 8:
# 	print "1", True
# else:
# 	print "1", False

# if 8 == "8":
# 	print "2", True
# else:
# 	print "2", False

# if 8 == 8.0:
# 	print "3", True
# else:
# 	print "3", False

# if "hi" == "hi":
# 	print "4 True"
# else:
# 	print "4", False

# if "HI" == "hi":
# 	print "5", True
# else:
# 	print "5", False

# if "HI" > "hi":
# 	print "6", True
# else:
# 	print "6", False

#2. Make expressions that evaluate to True using the following operators:

# if "meow" == "meow":
# 	print "1", True
# else:
# 	print "1", False

# if "meow" != "Meow":
# 	print "2", True
# else:
# 	print "2", False 

# if 9 > 2:
# 	print "3", True 
# else: 
# 	print "3", False 

# if 8 >= 8:
# 	print "4", True
# else: 
# 	print "4", False

# if 9 <= 10:
# 	print "5", True 
# else:
# 	print "5", False

#3. Make expressions that evaluate to False using the following operators:

# if "meow" == "Meow":
# 	print "1", True
# else:
# 	print "1", False

# if "1" != "1":
# 	print "2", True
# else:
# 	print "2", False

# if 10 > 20:
# 	print "3", True
# else:
# 	print "3", False

# if len("meow") < 4:
# 	print "4", True
# else:
# 	print "4", False

# if 200.45 >= 200.50:
# 	print "5", True
# else:
# 	print "5", False

# if 854 <= 800:
# 	print "6", True
# else:
# 	print "6", False

#4. Use the python interpreter to find out if the following boolean expressions are True.

# if True == True:
# 	print "1", True

# if False == False:
# 	print "2", True

# if 5 == True:
# 	print "3", True

# if 5 == False:
# 	print "4", True

# if bool(5) == True:
# 	print "5", True

# if "bye" == True:
# 	print "6", True

# if "bye" == False:
# 	print "7", True

# if bool("bye") == True:
# 	print "8", True

#4. Logical Operators
#4a. Test if 5 is greater than 9 and less than 3 using logical operators.

# if 5 > 9 and 5 < 3:
# 	print True
# else:
# 	print False

# if 10 <= 10:
# 	print True
# else:
# 	print False


# def food(tacos):
# 	# if tacos == True: 
# 	# 	print "<3<3<3"
# 	if not tacos:
# 		print "I need some tacos"

# food(False)

#Conditional Statements

# if len("Monique") > len("Thais"):
# 	print "My name is greater!"
# elif len("Thais") > len("Monique"):
# 	print "Their name is greater!"
# else: 
# 	print "Our names are equal!"

# todayfoo = datetime.date.today()
# day = todayfoo.day

day = datetime.date.today().day

print day
# print today
if day >= 15:
	print "Oh, we're halfway there!"
else:
	print "The month is still young!"

today = datetime.date.today()
day = today.day
print today












