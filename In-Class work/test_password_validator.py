import unittest

def password_strong_enough(password):
    """
    This function is (supposed to) return whether
    a password is ''strong'' enough, which is defined by 
       being 8-20 characters in length
       not containing any spaces

    """
    return len(password) >= 8 and " " not in password

class TestPassword(unittest.TestCase):

    def test_between_8_and_20(self):
        assert password_strong_enough("abcdefghij") == True
        assert password_strong_enought("Password") == False
        # Add another assert statement under this line 
        # It should be another password between 8 and 20 characters

    # Any new functions go here with same indentation

    # See if you can write a test that the function fails!



if __name__ == "__main__":
    unittest.main()
