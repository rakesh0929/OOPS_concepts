from oops_concept import day_2
from utils.util1 import Person1   ## utiles is package and util is a module and Person1 is a function

objects_imported_ustile_modules = Person1("hey","hi",9000)
print(objects_imported_ustile_modules.year)

object_2 = day_2.Person1("Mosh","H",3000)
print(object_2.year)
print(object_2._name)
print(object_2._Person1__surname)

class Person():

    _name = "Rakesh"
    __surname = "Raki"
    yob = 2001
    def age(self,current_year):
        return current_year - self.yob

    def _age(self,current_year):
        return current_year - self.yob

    def __age(self,current_year):
        return current_year - self.yob

obj = Person()
print(obj.yob)
print(obj._Person__age(2022))

class Employee(Person):
    _name = "Ravi"
    __surname = "Mosh",
    yob = 2000

object = Employee()
print(object._name)
print(object._Employee__surname)
print(object.age(2022))   ## Employee
print(obj.age(2022))  ## person
print(object._age(2024))   ## calling the employee and accessing the other protected value
'''calling the employee and accessing the other Private value'''
print(object._Person__age(2025))



