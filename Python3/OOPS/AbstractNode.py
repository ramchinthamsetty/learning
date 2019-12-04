from abc import ABC, abstractmethod

class AbstractNode(ABC): 
    """
    - Just declaring the Abstract methods. Pass ABC to class, so that it is not instantiated.
    """
    @abstractmethod
    def get_data(self):
        pass
    
    @abstractmethod
    def get_links(self):
        pass
    
class AbstractInterface(AbstractNode):
    """
     - Defining the methods from Inherited Abstract Class here.P
    """   
    def get_data(self):
        print("Defining the function here")
        return super().get_data() # Super will refer parent class definition here
    
    def get_links(self):
        print("Getting links info here")
        return super().get_links() # Super will refer parent class definition here

nodeval = AbstractInterface()
print(nodeval.get_data())    