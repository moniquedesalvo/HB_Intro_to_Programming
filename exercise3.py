 # This Python file uses the following encoding: utf-8

#Problem 2

#broken code, Can you spot the errors? please fix it
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "y"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#fix the code below
# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# what does the “,” do to the print output?
# makes a space
# what does the "+" do to the print output?
# adds the string next to another without a space
# what is the difference between how "+" is used here vs. line 55
# line 55 adds a float
new_string = end1 + end2 + end3 + end4 + end5 + end6 + " " + end7 + end8 + end9 + end10 + end11 + end12
#what do you think "print new_string" will output? it will add the letters but the " "  will add a space
print new_string

print new_string[0] # what do you thinking this line  will print?
# why, do you think? C because it's the 1st letter in the string and the range starts at 0
print new_string[1] # what do you thinking this line  will print?
# why, do you think? h
print new_string[-1] # what do you thinking this line  will print?
# why, do you think? r
