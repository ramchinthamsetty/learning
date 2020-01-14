

class Finder:
    
    def __init__(self, strings_in):
        self.string_patterns = strings_in
        
    def find_match(self, match_string):
        """
        match_string - Input value to match strings in the list
        @return - List if there are match of strings irrespective of order of characters in match_string
        """
        #Checking if the input value is string
        if not isinstance(match_string, str):
            raise TypeError("Value should be str")
        
        #Storing the length of match string here
        match_len = len(match_string)
        sorted_match_string = sorted(match_string)
        #Check if the value given is not an empty string
        if match_len == 0:
            raise ValueError("Value shouldn't be empty")
        
        result_list = []
        
        for each_string in self._get_each_string():
            print(each_string)
            each_str_len = len(each_string)
            # Check if string length matches with match string length.
            if match_len == each_str_len:
                each_sorted_string = sorted(each_string)
                # Match the string with sorted string
                if sorted_match_string == each_sorted_string:
                    result_list.append(each_string)
            else:
                continue
        
        return result_list
    
    def _get_each_string(self):
        """
        @return - Yields each string for the given strings list string_patterns
        """
        for each_string in self.string_patterns:
            yield each_string