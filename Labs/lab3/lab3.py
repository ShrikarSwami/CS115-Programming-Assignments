# === CS 115 Lab 3 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:
#
# Pledge:
#
from functools import reduce
# === CS 115 Lab 3 ===
#
# You are welcome and encouraged to define additional functions here.
# ---
def add(x,y):
    sum = x + y
    return sum
# ---

def mean(data):
    items = len(data)
    sum=reduce(add,(data))
    return sum/items



def rms(data):
    pass  # Delete this line, and write your own code here instead.


def hm(data):
    pass  # Delete this line, and write your own code here instead.


