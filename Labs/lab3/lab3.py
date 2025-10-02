# === CS 115 Lab 3 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
from functools import reduce
import math
# === CS 115 Lab 3 ===
#
# You are welcome and encouraged to define additional functions here.
# ---
def add(x,y):
    sum = x + y
    return sum

def square(x):
    return x ** 2

def real(x):
    if x is None:
        return False
    else:
        return True
def inverse(x):
    return (1/x)
# ---

def mean(data):
    items = len(data)
    sum=reduce(add,(data))
    return (sum/items)



def rms(data):
    data=list(filter(real,(data)))
    length=len(data)
    data=map(square,(data))
    total=reduce(add,(data))
    mean=total/length
    return math.sqrt(mean)

def hm(data):
    data=list(filter(real,(data)))
    length=len(data)
    data=map(inverse,(data))
    sum=reduce(add,(data))
    return length/sum


