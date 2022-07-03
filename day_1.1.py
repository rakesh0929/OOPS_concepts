class person:
    def age(self , current_year , data_of_birth):
        return  current_year - data_of_birth

    def emailid(self):
        email_id = input("Enter the mail id : ")
        return email_id

    def fullname(self,name):
        return name

m = person()
r = person()
print(m.emailid())








