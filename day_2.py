

class Person1():
    def __init__(self,name,surname,data_of_birth_year):
        self._name  = name                         ## _ single underscore before the vaiable self._name it is protected
        self.__surname = surname
        self.year = data_of_birth_year

rakesh = Person1("Rakesh","Raki",2001)
print(rakesh._name)
# print(rakesh.__surname)   ## __ private it will not exectue if you call print(classname.__variable)
print(rakesh._Person1__surname)   ## when your value is private then print(variable._classname__variable in class)
print(rakesh.year)

1


