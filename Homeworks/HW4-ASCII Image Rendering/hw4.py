# === CS 115 Homework 4 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 4 ===
from hw4_library import ppm_to_list_of_lists_of_rgbs, save_string_to_txt


def rgb_to_grayscale(image):
    """
    Mutates a 2D list of RGB pixels to a 2D list of grayscale values.
    Uses the CCIR 601 standard brightness formula:
        gray = int (0.299*red + 0.587*green + 0.114*blue)
    Does not return anything
    """
    for r in range(len(image)): # this loops each row index so we can replace the entire row
        new_row = [] #This is a fresh row so then later I can put in grayscale numbers
        for c in range(len(image[r])):#This line loops over each clumn index inside the row
            R, G, B = image[r][c] #This takes the rgb values form each pixel in an image
            val = int(0.299 * R + 0.587 * G + 0.114 * B) #These values are supposed to compute the brigthiness using the required weighted sum and then making that into an int
            if val < 0: #make sure no weird inputs
                val = 0 #0 is the least "brightest" something can be
            elif val>255: #safety so it doesn't have an alternative weird ouptut
                val=255 #255 is the most brightest something can be
            new_row.append(val) #Add this computed brightness to the new row
        image[r] = new_row #This replaced the old RGB row with the new gray one in its place
        

def brightness_to_ascii(brightness):
    """
    TODO: Fill in your own docstring here based on 
    the homework description
    Use the table on the homework for specific ranges
    of brightness to ASCII
    """
    b = int(brightness)# Make sure we are working with an integers (only real base case for this one)
    if b < 0:# Nothing below 0
        b = 0# bring it to a nice range
    if b > 255:# nothing above 255
        b = 255# bring it to a nice range

    if b <= 25:# 0 to 25 maps to the darkest character
        return '@'# Return the correct character for this range
    elif b <= 51:# 26 to 51
        return '#'
    elif b <= 76:# 52 to 76
        return '%'
    elif b <= 102:# 77 to 102
        return '*'
    elif b <= 127:# 103 to 127
        return '='
    elif b <= 153:# 128 to 153
        return '+'
    elif b <= 179:# 154 to 179
        return '-'
    elif b <= 204:# 180 to 204
        return ':'
    elif b <= 230:# 205 to 230
        return '.'
    else:# 231 to 255
        return ' '# The lightest value is a space
    #This was lowkey the best function to write cuz its the most fun in my opinion

    


def image_to_ascii_string(grayscale_image):
    """
    Convert a 2D list of grayscale values (0–255)
    into a single string of ASCII characters where
    each row in the image corresponds to a line
    in the ASCII string. 

    Each line break is represented with \n\r
    to ensure compatibility with Windows 
    
    returns that string, only containing valid ASCII
    characters
    """
    lines = [] #collect text for each row
    for row in grayscale_image: #Go row by row through the imgae
        chars = [brightness_to_ascii(v) for v in row] #conver each brightness in a row to a character
        line = ''.join(chars) #This should put all the characters togheter to form one line
        lines.append(line) #store the finished line
    return "\r\n".join(lines)#Join all the lines using different string unctions so it is displayed correctly
    

def invert(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    for r in range(len(image)):# Gp trough every row
        for c in range(len(image[r])):# Go through every column
            image[r][c] = 255 - int(image[r][c])# Invert and store it back



def lighten(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    for r in range(len(image)):# Loop through rows
        for c in range(len(image[r])):# Loop through columns
            v = int(round(image[r][c] * 1.3))# Scale up by 1.3 with rounding for nice values
            if v > 255:# Make sure it doesn't go over 255
                v = 255# fix it if it does
            image[r][c] = v# Store the result back into the image

    


def darken(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    for r in range(len(image)):# Loop through rows
        for c in range(len(image[r])):# Loop through columns
            v = int(round(image[r][c] * 0.7))# Scale down by 0.7 with rounding
            if v < 0:#don't fo under 0
                v = 0# Fix it if it does go under 0
            image[r][c] = v# Store the result back into the image



def erase(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    for r in range(len(image)):# Loop through rows
        for c in range(len(image[r])):# Loop through columns
            image[r][c] = 0# Set the pixel to black so it is as though it has been "erased"



def load_rgb_image(image_name):
    """
    Given a filename, image_name, returns 
    a grayscale image, 
    represented as a 2D list of intensities

    Do not change this function. It is just here for reference.
    """
    image = ppm_to_list_of_lists_of_rgbs(image_name)
    return image 


if __name__ == "__main__":
    # All code you want to run goes in this indented block
    # You can change the name of ppm_image_filename
    ppm_image_filename = "small_secret_image.ppm"

    # This line calls our library function to load the image as 
    # a list of lists of rgb values
    image = load_rgb_image(ppm_image_filename)

    # Uncomment this line for Task 1
    # 
    rgb_to_grayscale(image)

    # Uncomment this line for Task 2
    # 
    ascii_string = image_to_ascii_string(image)

    # Uncomment this to save your ascii string to a text file
    # which can be read in other applications and uploaded
    # to Gradescope
    # 
    save_string_to_txt(ascii_string, "treasure_map.txt")
