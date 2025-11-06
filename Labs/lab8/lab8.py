# === CS 115 Lab 8 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 8 ===
def copy_3d(lll):
    return list(map(lambda mid: list(map(lambda inner: inner[:], mid) ), lll)) #This uses the higher order function lambda to recursively copy each item within the list


def check(x):
    """
    This is a helper function that basically just gives me id as an int for me to compare
    """
    return id(x)

def check_copy_3d(lll_1, lll_2):
    if isinstance(lll_1,list) and isinstance(lll_2, list): #Base case to make sure that the items are lists
        if check(lll_1)==check(lll_2): #This is a base case that makes sure the two lists aren't pointing to the same memory
            return False #If it does point to the same memory it throw back and error
        if len(lll_1)!=len(lll_2): #If the lists are not same in size they cannot be a deep_copy
            return False #That also returns an error
        compare = map(lambda a, b: check_copy_3d(a, b), lll_1, lll_2) #This compares the id's of everything within the list going list by list then item by item within that list and then returinng all like [true, true, true] = True
        return all(compare)
    return lll_1==lll_2
    
