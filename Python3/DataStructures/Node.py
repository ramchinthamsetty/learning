
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self,newnext):
        self.next = newnext






