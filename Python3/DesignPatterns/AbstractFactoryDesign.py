from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass
    
class ConcreteFactory2(AbstractFactory):
    """
    Inheritance of AbstractFactory Class
    """
    
    def create_product_a(self):
        return ConcreteProductA2()
    
    def create_product_b(self):
        return ConcreteProductB2()


class ConcreteFactory1(AbstractFactory):
    """
    Inheritance of AbstractFactory Class
    """
    
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()
    

class AbstractProductA(ABC):
    
    @abstractmethod
    def useful_function_a(self):
        pass
    

class ConcreteProductA1(AbstractProductA):
    
    def useful_function_a(self):
        return "The result of the product A1"
    
class ConcreteProductA2(AbstractProductA):
    
    def useful_function_a(self):
        return "The result of the product A2"
    

class AbstractProductB(ABC):
    
    @abstractmethod
    def useful_function_b(self):
        pass
    
    
    @abstractmethod
    def another_useful_function_b(self,collaborator: AbstractProductA):
        pass
    
class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "This is result of product B1"
    
    def another_useful_function_b(self, collaborator):
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"
    

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "This is result of product B1"
    
    def another_useful_function_b(self, collaborator):
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"    



def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")
    
if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())    