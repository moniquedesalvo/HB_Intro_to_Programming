#refer to string_formats.py Problem 1b

my_name = str(raw_input("What is your name? "))
my_height = float(raw_input("What is your height in inches? "))
pet_age = int(raw_input("How old is your pet? "))
pet_eyes = str(raw_input("What color are your pet's eyes? "))
pet_hair = str(raw_input("What color is your pet's hair? "))
pet_name = str(raw_input("What is your pet's name? "))
pet_weight = int(raw_input("How much does your pet weigh? "))

print "Hi %s, how tall are you?" % (my_name)

print "I'm %.2f inches tall." % (my_height)

print "My pet's name is %s." % (pet_name)

print "%s is %i years old." % (pet_name, pet_age)

print "She's actually %i pounds heavy." % (pet_weight)
print "Actually, that's not too %s." % ("heavy")

print "My pet has %s eyes and %s hair." % (pet_eyes, pet_hair)

print "If I add %.2f and %i, I get %.2f." % (my_height, pet_weight, my_height + pet_weight)