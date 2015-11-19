sunday = int(raw_input("How many steps did you take on Sunday? "))
monday = int(raw_input("How many steps did you take on Monday? "))
tuesday = int(raw_input("How many steps did you take on Tuesday? "))
wednesday = int(raw_input("How many steps did you take on Wednesday? "))
thursday = int(raw_input("How many steps did you take on Thursday? "))
friday = int(raw_input("How many steps did you take on Friday? "))
saturday = int(raw_input("How many steps did you take on Saturday? "))

#for each 1000 steps * "*""

print "Sunday    " + sunday/1000 * "*"
print "Monday    " + monday/1000 * "*"
print "Tuesday   " + tuesday/1000 * "*"
print "Wednesday " + wednesday/1000 * "*"
print "Thursday  " + thursday/1000 * "*"
print "Friday    " + friday/1000 * "*"
print "Saturday  " + saturday/1000 * "*"


goal = int(raw_input("What is your weekly step goal? "))

goal_progress = sunday + monday + tuesday + wednesday + thursday + friday + saturday
print goal_progress


if goal_progress < goal:
	print "You couch potato! Get out and go for a walk!"
elif goal_progress >= goal:
	print "Wow! You've met your goal! Keep up the good work!"


goal = int(raw_input("What is your daily step goal? "))	
days_met = 0

print "You met your goal on:" 

if goal <= sunday:
	print "Sunday"
	days_met = days_met + 1

if goal <= monday:
	print "Monday"
	days_met = days_met + 1

if goal <= tuesday:
	print "Tuesday"
	days_met = days_met + 1

if goal <= wednesday:
	print "Wednesday"
	days_met = days_met + 1

if goal <= thursday:
	print "Thursday"
	days_met = days_met + 1

if goal <= friday:
	print "Friday"
	days_met = days_met + 1

if goal <= saturday:
	print "Saturday"
	days_met = days_met + 1

#for each day the goal was met add 1
print "That's %i out of 7 days!" % days_met

if days_met >= 5:
	print "Congratulations! You've met your goal for most of the week!"
else:
	print "You really need to get out more."





