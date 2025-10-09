# === CS 115 Homework 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System. 
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
    return "?" #This is what happens when nothing is found or it breaks 

def code_to_letter(code): #so above there is the letter_to_code this is like the reverse of that
    matching_pairs = tuple(filter(lambda pair: pair[0] == code, morse)) #again similar to the first one but what it does it looks for like the codes htat are in the morse list and then removes everything that is not in the word
    if matching_pairs: #Then wiht the matching pairs (that hopefully exist) it begins to "convert" them within this if statement
        first_pair=matching_pairs[0]
        letter = first_pair[1]
        return letter
    return "?"
#Overally this is very similar to the previous function just swaping what it does 



# Uncomment one of the following lines to try your code
# with a larger dictionary of words:
#from dict import dictionary
#from bigdict import dictionary

def encode(plaintext):
    text = plaintext.upper() #Converts whatever the word is to upper case (ik its not nessasary but I am trying to acc think about things like this)
    letters = tuple(text) #This turns it into a tuple so like "HI" becomes ['H', 'I']
    codes_iterations = map(lambda character: letter_to_code(character), letters) #This line should build an iterator that basically uses the function I wrote earlier to translate each character of the tuple in its Morse counterpart 
    codes = tuple(codes_iterations) #This actually creates a tuple with the codes so for "HI" it turns it into like ['....', '..'] 
    encoded_code=" ".join(codes)#This takes the tuple from the line above and makes it an actual line of code like .... ..
    return encoded_code #just returns the code and whatnot

    

def decode(cyphertext):
    short = cyphertext.strip() #This isn't in the first one but the thing is that all the morse code has to come in with spaces unlike a word the strip command (even tho not nessasary) is being used to make sure there is no spaces at the start of the code
    items = short.split(" ") #The next line is quite similar in the sense it removes the spaces so that it can create one single string of the code
    thing = tuple(filter(lambda t: t != "", items)) #Then what happens is that it creates a list of each individual unique code so that it can then be back translated into whatever it is meant to be
    letter_iterations = map(lambda line: code_to_letter(line), thing) #This is the line that actually then finds each comparision and compares like which code has which letter
    letters = tuple(letter_iterations) #This then turns each indivdiual code into a list item 
    decoded = "".join(letters) #This is joiining the whole thing into a single word now that each code hasbeen traslated
    return decoded #This finally is meant to return the decoded text as regular words and whatnot

def matches(cyphertext):
    target = cyphertext
    def encode_without_any_spaces(word): #This little function here will first encode things then like remove spaces to then allow us to compare them to the target.
        morse_with_spaces = encode(word)
        morse_no_spaces = morse_with_spaces.replace(" ", "")
        return morse_no_spaces
    keep_word = lambda w: encode_without_any_spaces(w) == target #This keeps a word if its space free and encodes it with equals to the target.
    filtered_words_iterations = filter(keep_word, dictionary) #This filters the dictionary above using the keep_word test
    result = tuple(filtered_words_iterations) #Materialize into a tuple so basicaly the tests want something iterable as well as stable
    return result #Return the matching word and if there is none it should return as just empty 
    
    
