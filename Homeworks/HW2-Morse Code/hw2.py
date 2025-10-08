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

def code_to_letter(code): #so above there is the letter_to_code this is like the reverse of that
    matching_pairs = tuple(filter(lambda pair: pair[0] == code, morse)) #again similar to the first one but what it does it looks for like the codes htat are in the morse list and then removes everything that is not in the word
    if matching_pair: #Then wiht the matching pairs (that hopefully exist) it begins to "convert" them within this if statement
        first_pair=matching_pairs[0]
        code = first_pair[0]
        return code
    return "Error"
#Overally this is very similar to the previous function just swaping what it does 



# Uncomment one of the following lines to try your code
# with a larger dictionary of words:
#from dict import dictionary
#from bigdict import dictionary

def encode(plaintext):
    text = plaintext.upper() #Converts whatever the word is to upper case (ik its not nessasary but I am trying to acc think about things like this)
    letter = tuple(text) #This turns it into a tuple so like "HI" becomes ['H', 'I']
    codes_iterations = map(lambda ch: letter_to_code(letter), letters) #This line should build an iterator that basically uses the function I wrote earlier to translate each character of the tuple in its Morse counterpart 
    codes = tuple(codes_iterations) #This actually creates a tuple with the codes so for "HI" it turns it into like ['....', '..'] 
    encoded_code=" ".join(codes)#This takes the tuple from the line above and makes it an actual line of code like .... ..
    return encoded_code #just returns the code and whatnot

    

def decode(cyphertext):
    pass # Delete this line, and write your own code here instead.

def matches(cyphertext):
    pass # Delete this line, and write your own code here instead.
