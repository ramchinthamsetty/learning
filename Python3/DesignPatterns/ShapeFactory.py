'''
 - Create a Factory Design pattern
'''

class ShapeInterface:
    def draw(self): pass
    

class Circle(ShapeInterface):
    def draw(self):
        print("Circle is drawn")
        return 

class Square(ShapeInterface):
    def draw(self):
        print("Square is drawn")
        return

class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == "Circle":
            return Circle()
        elif type == "Square":
            return Square()
        assert 0,"Could not find shape "+type

            
