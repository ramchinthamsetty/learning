import unittest
from  Relayr.src.Finder import Finder
class FinderTests(unittest.TestCase):
    
    def setUp(self):
        self.alphan_strings = [
                        "asd",
                        "1asd",
                        "asdf",
                        "sad",
                        "das",
                        "1234asdf"
                        ]
        self.special_strings = [
                        "@!123asdf",
                        "@123",
                        "sad sad",
                         "123asd 123asd"
                                ]
        self.alphan_obj = Finder(self.alphan_strings)
        self.special_obj = Finder(self.special_strings)
        
    
    def tearDown(self):
        pass
    
    def test_alphanumeric_strings(self):
        """
        Test cases to test alpha numeric characters
        """
        aplha_string = "asdf"
        alphan_string = "1asd"
        alpha_string1 = "den"
        aplhan_string1 = "12asd"
        self.assertEqual(self.alphan_obj.find_match(aplha_string), ["asd","sad","das"])
        
    
    def test_special_strings(self):
        """
        Test cases to test special character based strings containing !@#$^&*()
        """
        pass
    
    def test_space_contained_strings(self):
        pass
    
    def test_unprintable_strings(self):
        '''
        Test case to raise exceptions when Strings contain '\n\t' or escape sequences
        https://realpython.com/python-strings/#built-in-string-methods
        '''
        pass
        
    def test_numerical_values(self):
        """
        Test cases if the string given is numerical values or digits.
        """
        pass
    
    if __name__ == "__main__":
        unittest.main()