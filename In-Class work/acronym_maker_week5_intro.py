from functools import reduce

def word_processor(x):
    """
    Given input x, capitalizes it, then returns the first letter
    """
    return to_upper(x[0])

def combine_strings(str1, str2):
    """ Takes two strings and returns them concatenated / combined """
    return str1 + str2

def my_filter_function(x):
    return not is_stop_word(x) and is_alpha(x)

def acronym_maker(word_list):
    """
    Given a list of words (which may include words with numbers)
    return a single string acronym with:
         - all capital letters
         - the first letter of each *word* with only alphabetic characters*
    """

    filtered_word_list = list(filter(my_filter_function, words)) # Remove [] and write your filter code here
    print("Filtered words: " + str(filtered_word_list))
   
    # Calls the word_processor on filtered_word_list 
    processed_words = list(map(word_processor, filtered_word_list))

    print("Processed words: " + str(processed_words))
    
    # Reduces the processed words to a single string using combine_strings
    acronym = [] # Remove [] and write your reduce code here
    
    print("Acronym after reduce: " +  str(acronym))

    return acronym



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

    # For part 2 
    print("Acronym: "+ str(acronym_maker(words)))
