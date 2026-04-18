# Parent class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # if we don't want to show age and make privacy for it we can simply write:
        # self.__age = age instead of self.age = age

    def display(self):
        print(self.name, self.age)