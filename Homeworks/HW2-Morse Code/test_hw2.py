import hw2
import unittest

hw2.dictionary = ("AM", "AS", "BE", "BED", "CAN", "EGG", "HE", "HER", "HIM",
    "HIS", "ILL", "IS", "KID", "ME", "MY", "ON", "OR", "SEE", "SO", "TO",
    "TOE", "TOW", "WAS", "WOW",)
# For testing purposes,
# we install the standard dictionary here.

class TestCases(unittest.TestCase):
    def test_encode_case_1(self):
        inp = "AM"
        out = ".- --"
        self.assertEqual(hw2.encode(inp), out)

    def test_encode_case_2(self):
        inp = "CAN"
        out = "-.-. .- -."
        self.assertEqual(hw2.encode(inp), out)

    def test_encode_case_3(self):
        inp = "SEE"
        out = "... . ."
        self.assertEqual(hw2.encode(inp), out)

    def test_encode_case_4(self):
        inp = "GLOW"
        out = "--. .-.. --- .--"
        self.assertEqual(hw2.encode(inp), out)

    def test_decode_case_1(self):
        # Your test cases should go here.
        # Feel free to create additional methods as needed.
        pass

    def test_matches_case_1(self):
        inp = "-.-..--."
        out = ("CAN",)
        self.assertCountEqual(hw2.matches(inp), out)

    def test_matches_case_2(self):
        inp = "....."
        out = ("SEE", "HE", "IS",)
        self.assertCountEqual(hw2.matches(inp), out)

    def test_matches_case_3(self):
        inp = "................"
        out = ()
        self.assertCountEqual(hw2.matches(inp), out)

    def test_matches_case_4(self):
        inp = "----."
        out = ("ON", "TOE",)
        self.assertCountEqual(hw2.matches(inp), out)

if __name__ == "__main__":
    unittest.main()
