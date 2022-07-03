class Person():

    def __init__(self,name,email_id,surname,year_of_birth):
        self.name = name
        self.mail  = email_id
        self.sur = surname
        self.year = year_of_birth

    def aadhar(self,number):
        if number == 123456789 and self.mail == f"{self.name.lower()}@gmail.com":
            return self.name

    def age(self,current_year):
        return f'you are {current_year - self.year} years old'

p1 = Person("Mosh","mosh@gmail.com","Hari",2001)
print(p1.aadhar(123456789))
print(p1.age(2022))
print(p1.name)
print(p1.year)
print(p1.sur)
print(p1.mail)



