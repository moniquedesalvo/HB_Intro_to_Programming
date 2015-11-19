print "Welcome to the survey! :)"
name1=raw_input("What's your name?")
name2=raw_input("What's your pair's name?")


print "Hello %s and %s!"%(name1,name2)
color1=raw_input("What is your favorite color, %s?"%(name1))
color2=raw_input("What is your favorite color, %s?"%(name2))
hobby1=raw_input("What's your favorite hobby, %s?"%(name1))
hobby2=raw_input("What's your favorite hobby, %s?"%(name2))
movie1=raw_input("What's your favorite movie, %s?"%(name1))
movie2=raw_input("What's your favorite movie, %s?"%(name2))
age1=raw_input("How old are you?, %s?"%(name1))
age2=raw_input("How old are you?, %s?"%(name2))
drink1=raw_input("Beer or wine?, %s?"%(name1))
drink2=raw_input("Beer or wine, %s?"%(name2))

print name1, "is", age1+ ".", "Her favorite color is",color1,"and",hobby1,"is her hobby."+" "+"Her favorite movie is %s and she prefers %s."%(movie1, drink1)
print name2, "is", age2+ ".", "Her favorite color is",color2,"and",hobby2,"is her hobby."+" "+"Her favorite movie is %s and she prefers %s."%(movie2, drink2)