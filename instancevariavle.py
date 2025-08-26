# instance variable
class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def talk(self):
        print(f"{self.name} is able to talk")

myobj = Student('prabesh',22,'Bhaktapur')
print(myobj.name)
print(myobj.talk())