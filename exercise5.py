# Problem 4
#1) Broken code: fix the syntax and other errors in this code, 
#2) comment on what each line of code is doing
#please assign values to the variables' 
my_name = "Monique"
my_height = 63
pet_age = 10
pet_eyes = "green"
pet_hair = "multi-colored"
pet_name = "Charlene"
pet_weight = 7

def string_formatting():  #defining a function, this line is correct --do not change 
    number = input("what's your favorite integer? ")
    food = raw_input("what's your favorite food? ")
    print my_name * pet_age  # Monique * 10
    print type(my_height)   # the type of my height is int
    print bool(pet_eyes)     # True, because there's a value
    print bool(pet_hair) + bool(pet_name)  # true + true = 1 + 1 = 2
    print float(pet_weight) # turns pet weight into a float
    print "i love {} ".format(food) * number  # multiplies food variable value by my fav number variable value

string_formatting()    #calling / activating a function, this line is correct --do not change 

"""
goals: scaffold function block format, syntax error debugging, commenting,

"""
