# === CS 115 Lab 6 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 6 ===
def to_int(tup, base): #This is the line defining the function
    if len(tup) == 1: #This is a base case that checks if there is only one value and if there is return the same thing
        return tup[0]
    else: #This is the actual part of the program that uses recursion to check add up each value
        length = len(tup)
        return tup[0]*base**(length-1)+ to_int(tup[1:], base) #This is the recursive statement that takes the value, multiply if by the base to the power of whatever the length 
    

def to_base(n, base):
    if n == 0:
        return (0,)
    elif n<base:
        return (n,)
    else:
        tup = []
        quotient = n//base
        remainder = n%base
        return to_base(quotient, base) + (remainder,)
        
            
 
