class MyPropertyValidation(object):
    def __init__(self):
        self.__age = None

    @property
    def age(self):
        if not self.__age:
            raise ValueError("Age is None and needs to be set first.")
        return self.__age

    @age.setter
    def age(self, val):
        if isinstance( val, int ) and val > 0:
            self.__age = val
        else:
            raise ValueError("Age needs to be an integer and greater than zero")