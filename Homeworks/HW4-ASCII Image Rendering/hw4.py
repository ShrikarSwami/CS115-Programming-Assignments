# === CS 115 Homework 4 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:
#
# Pledge:
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
    raise NotImplementedError()

def brightness_to_ascii(brightness):
    """
    TODO: Fill in your own docstring here based on 
    the homework description
    Use the table on the homework for specific ranges
    of brightness to ASCII
    """
    raise NotImplementedError()


def image_to_ascii_string(image):
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
    raise NotImplementedError()

def invert(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    raise NotImplementedError()


def lighten(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    raise NotImplementedError()


def darken(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    raise NotImplementedError()


def erase(image):
    """
    TODO: Fill in your own docstring here based on 
    the homework description

    Does not return anything. Only mutates the input.
    """
    raise NotImplementedError()

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
    # rgb_to_grayscale(image)

    # Uncomment this line for Task 2
    # 
    # ascii_string = image_to_ascii_string(grayscale_image)

    # Uncomment this to save your ascii string to a text file
    # which can be read in other applications and uploaded
    # to Gradescope
    # 
    # save_string_to_txt(ascii_string)
