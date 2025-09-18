# === CS 115 Lab 01 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 01 ===
def consecutive_sum(x, y):
    """
    The function takes in the inputs x & y inputs as the lower and upper bounds then plugs in the numbers into a forumla to calculate the sum of all the numbers between the upper and lower bound. We also assume all numbers are greater than zero and both x and y are whole numbers
    """
    distance = (y-x)
    sum=(y+x-1)/2
    sum=sum*distance
    return sum


def same_ends(word):
    """
    The input is a word, before anything it converts the word to a lower case to avoid issues with a word like "Nun" returing false, Then is creates a variable for the length of the string and uses that when comparing the first and last letter. Once it does that it either returns True or False. You also assume that the text is only comprised of letters, numbers, and spaces
    """
    word=word.lower()
    length=len(word)
    if word[0:1] == word[length-1:length]:
        return True
    else:
        return False
    

def is_palindromic(word):
    """
    The input for this program is a word, before anything it converts it to lowercase, then once it converts it then reverses the word and compares the two and based off it is the same it then returns True or False. You are assuming that the user is only entering letter, numbers and spaces.
    """
    word=word.lower()
    word_reverse=word[::-1]
    if word==word_reverse:
        return True
    else:
        return False

def get_ticket_price(age):
    """
    For this program we compare the age to the various ranges and based off the range in which the number falls it will return the corresponding price for that.
    """
    if age<3:
        return 0
    elif age<13:
        return 10
    elif age<65:
        return 15
    elif age>=65:
        return 12
    else:
        return None

        
