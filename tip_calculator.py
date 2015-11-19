def calculate_tip(total_bill):
	return total_bill * .20

print "%.2f" % calculate_tip(42.50)

def calculate_tip2(total_bill, tip_percent):
	return total_bill * tip_percent

print "%.2f" % calculate_tip2(42.50, .2)
print "%.2f" % calculate_tip2(58.30, .15)

def tips_with_friends(total_bill, tip_percent, num_friends):
	return (total_bill * tip_percent)/num_friends

print "Each person should pay %.2f." % tips_with_friends(42.50, .2, 2)