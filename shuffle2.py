import inspect


# Write a pseudo-code description [a list of the steps you would need to do to
# solve the problem, no python wrangler skills necessary!] of a function that
# reverses a list of n integers, so that the numbers are listed in the
# opposite order than they were before, and compare this method to an
# equivalent Python function for doing the same thing.

# After you figure out the steps, can you figure out how to reverse the list
# in python with the built-in function and without the built-in function

# n = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

#for n return the last number then the second to last number, than third to last number, etc
# get length of list


n = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

# n.reverse();
# print n

# reverse = list(reversed(n))
	
# print reverse


# def backwards(list1):
# 	return list1 [::-1]
		

# print backwards(n)
	
# my_list = ["albert", "bob", "cynthia", "dan", "elvis", "frogger"]
# #http://pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
# # start:end:step
# print my_list[2:5:2]

# def backwards(list1):
# 	for i in list1:
# 		# length = len(list1)
# 		# return 
# 		return i


# print backwards(n)

# def back(list2):
# 	for i in list2:
# 		return i

# print list.back(n)

# for i in n:
# 	print i

n = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]


def backwards(list1):
	result = []
	length = len(list1)
	list_range = range(0,length)

	for i in list_range:
		new = list1[length - 1 - i]
		result.append(new)
	return result


print backwards(n)





