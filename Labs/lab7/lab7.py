import struct
# === CS 115 Lab 7 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 7 ===
def lagrassian_cipher(words, k):
    """
    Recursively apply the greatest cipher rule to each character in a string inside the tuple
    """
    def shift_char(c): #Shift exactly by one chracter k based off the partiy of its code point
        code=ord(c) #turn each character into a code point
        if code % 2 == 0:#even code 
            return chr(code + k) #move forward by k
        else: #Odd code point
            return chr(code - k) #move backwards by k
    def transform_string(s):
        if s == "": #empty base case
            return""
        first = s[0]
        rest = s[1:]
        return shift_char(first) + transform_string(rest)
    def transform_tuple(t):
        if len(t) == 0:
            return () #Base case for empty typle
        head = t[0] #first string
        tail = t[1:] #remainder of strings
        return (transform_string(head),) + transform_tuple(tail)#Do one, recurse
    
    return transform_tuple(words) #Kick off the reucsion on the tuple
    



### Helper functions (do not edit)
def print_bytes_as_bits(bytes):
    """Given Python bytes data, prints them as bits
    grouped by bytes"""
    bits_as_string = ' '.join(f'{b:08b}' for b in bytes)
    print(bits_as_string)


def pack_data(data, byte_order, number_format):
    """
    Packs the data in data as a number_format (ex. int)
    the order of bytes is specified by the variable byte_order.

    Valid number_formats include int, unsigned int, float, double
    """
    byte_order_to_byte_order_char = {"native": "@", "little endian": "<", "big endian": ">", "network": "!"}
    c_type_to_format = {"char": "c", "bool": "?", "short": "h", "int": "i", "unsigned int": "I", "long": "l",
                        "float": "f", "double": "d"}
    if byte_order not in byte_order_to_byte_order_char:
        raise ValueError(f"{byte_order} not in list of supported byte orders: {byte_order_to_byte_order_char.keys()}")
    if number_format not in c_type_to_format:
        raise ValueError(f"{number_format} not in list of supported number formats: {c_type_to_format.keys()}")
    format_string = byte_order_to_byte_order_char[byte_order] + c_type_to_format[number_format]
    return struct.pack(format_string, data)

if __name__ == '__main__':
    print()
    # your testing code should stay indented in this block
    # if you run lab7.py, this code will run
    # but it won't run if we import your functions
    #
    # for example, if you uncomment the code below, it will print the bits in the float representation of 0.25
    # data_in_bytes = pack_data(0.25, "network", "float")
    # print_bytes_as_bits(data_in_bytes)
