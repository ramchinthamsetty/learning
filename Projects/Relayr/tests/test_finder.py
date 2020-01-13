import unittest

class FinderTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_alphanumeric_strings(self):
        """
        Test cases to test alpha numeric characters
        """
        pass
    
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