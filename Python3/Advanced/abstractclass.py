import abc
"""
Abstraction Explained here
"""
class Shape:
    """
    Shape is an Abstract class
    """
    def get_sides(self):
        '''
        Abstract Method to get sides
        '''
        print("This method gives shape of the Object")
        pass

class Square(Shape):
    """
    Inheritance of Shape Class and Define Abstract Methods
    """
    def get_sides(self):
        #Super calls will call the base function defined in Shape Class
        super().get_sides()
        print("I have four sides")
        return 

class Triangle(Shape):
    """
    Inheritance Shape Class and Define Abstract Methods
    """
    def get_sides(self):
       print("I have three sides")

#Initialize the Objects 
triangle = Triangle()
squarebox = Square()

#xCall the defined functions of Abstract class
triangle.get_sides()
squarebox.get_sides()

