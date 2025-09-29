from functools import reduce


def acronym_maker(word_list):
    """
    Given a list of words (which may include words with numbers)
    return a single string acronym with:
         - all capital letters
         - the first letter of each *word* with only alphabetic characters*
    """
    # Your code here. It is up to you to define any local functions and 
    # know when to call map, filter, and reduce
    pass 


def to_upper(word):
    """ Returns the word but with every letter in uppercase"""
    return str.upper(word)

def is_alpha(word):
    """
    Given a string input, returns whether the word contains
    only alphabetic characters 
    """
    return word.isalpha()

def is_stop_word(word):
    return word in ["of", "the", "a", "to"]


if __name__ == '__main__': # Good practice: runs code in here when you run this file
    words = ["Gatehouse", "of", "1800", "obFuScaTed", "Discoveries", "under", "the", "CS-115's", "el33t", "computer", "Kruft", "$41$", "servers"] 

    print("Acronym: "+ str(acronym_maker(words)))
