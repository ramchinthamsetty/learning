class Finder:
    
    def __init__(self, Strings):
        self.string_patterns = Strings
        
    def find_match(self, match_string):
        """
        match_string - Input value to match strings in the list
        @return - List if there are match of strings irrespective of order of characters in match_string
        """
        
        return []