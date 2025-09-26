def acronym_maker(word_list):
    """
    Given a list of words (which may include words with numbers)
    return a single string acronym with:
         - all capital letters
         - the first letter of each *word with only alphabetic characters*
    """
    pass # Replace pass with your code



def to_upper(word):
    """ Returns the word but with every letter in uppercase"
    return str.upper(word)
    """

def is_alpha(word):
    """
    Given a string input, returns whether the word contains
    only alphabetic characters 
    """
    return word.isalpha()

if __name__ == '__main__': # Good practice: runs code in here when you run this file
    words = ["gatehouse", "CS-115", "opposite", "disCoVery", "US480", "under", "cApTaIn", "1337", "Krusty Krab", "$5", "stampede"]

    filtered_words = [] # Filter code here
   
    # For part 2 
    print(f"Acronym: {acronym_maker(words)}") # Modern string formatting
