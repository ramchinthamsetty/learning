from abc import ABC
class Math(ABC):
    
    def multiply_func(self):
          pass
    
    def subract_func(self):
        pass
    
    def addition_func(self):
        pass
    
    def squares_func(self):
        pass
    
    def factorial_func(self):
        pass
    
class MathOps(Math):
    
    def multiply_func(self, x, y):
        '''
        In - Self, X, Y - integer variables for muplication
        @return - Returns the muplication output value.
        '''    
        return x * y
    
    
    
    
    