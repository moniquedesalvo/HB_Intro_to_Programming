# Problem 5
"""
Take it further:
Many student use the command line as a game interface
(ie tic-tac-toe, battleship, hangman)

make a tic-tac-toe board using string characters and format 
#each of the nine squares with an integer in the middle using a 
string formatting technique

expected output:

   1   |  2   |  3   
---------------------
   4   |  5   |  6  
---------------------
    7  |  8   |  9
 
 Take it even further!!!:
 use variables assigned values from raw_input() to format each square's label  
 instead of numbers. adjust the spacing as necessary to keep the tic-tac-toe
 board shape
 
 goals: problem solving, string formatting, introduce projects types, introduce
 raw_input(), variables, multiple line strings
 
"""
A1 = raw_input("Type the number 1 ")
A2 = raw_input("Type the number 2 ")
A3 = raw_input("Type the number 3 ")
B1 = raw_input("Type the number 4 ")
B2 = raw_input("Type the number 5 ")
B3 = raw_input("Type the number 6 ")
C1 = raw_input("Type the number 7 ")
C2 = raw_input("Type the number 8 ")
C3 = raw_input("Type the number 9 ")

print "  {}  |  {}  |  {}  ".format(A1, A2, A3)
print "-" * 17
print "  {}  |  {}  |  {}  ".format(B1, B2, B3)
print "-" * 17
print "  {}  |  {}  |  {}  ".format(C1, C2, C3)
