# === CS 115 Homework 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 2 ===
morse = (
    ('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'), ('-..', 'D'), ('.', 'E'),
    ('..-.', 'F'), ('--.', 'G'), ('....', 'H'), ('..', 'I'), ('.---', 'J'),
    ('-.-', 'K'), ('.-..', 'L'), ('--', 'M'), ('-.', 'N'), ('---', 'O'),
    ('.--.', 'P'), ('--.-', 'Q'), ('.-.', 'R'), ('...', 'S'), ('-', 'T'),
    ('..-', 'U'), ('...-', 'V'), ('.--', 'W'), ('-..-', 'X'), ('-.--', 'Y'),
    ('--..', 'Z')
)

dictionary = ("AM", "AS", "BE", "BED", "CAN", "EGG", "HE", "HER", "HIM",
    "HIS", "ILL", "IS", "KID", "ME", "MY", "ON", "OR", "SEE", "SO", "TO",
    "TOE", "TOW", "WAS", "WOW",)

def letter_to_code(letter):
    matching_pairs = tuple(filter(lambda pair: pair[1] == letter, morse)) #keep only pairs from morse in which the second item (or the letter) matches the letter in the word
    if matching_pairs: #Once it gets rid of every single letter that DOESN't match it then goes ahead and gets the morse code values
        first_pair = matching_pairs[0] #This is taking the first pair
        code = first_pair[0] #Then swapping the Letter to code
        return code #This returns the morse
    return "Error" #This is what happens when nothing is found or it breaks 

# Uncomment one of the following lines to try your code
# with a larger dictionary of words:
#from dict import dictionary
#from bigdict import dictionary

def encode(plaintext):
    plaintext = plaintext.upper() #Converts this to uppercase
    letters = list(plaintext) #Takes the letters into individual list "HELLO" = ['H','E','L','L','O']

    

def decode(cyphertext):
    pass # Delete this line, and write your own code here instead.

def matches(cyphertext):
    pass # Delete this line, and write your own code here instead.
