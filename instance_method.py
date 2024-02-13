# instance methon 

class Person:
    def __init__(self,First_name,Last_name,age):
        self.First_name = First_name
        self.Last_name = Last_name
        self.age = age 

    def full_name(self):  # create a instance method (function )
        return self.First_name+' ' +self.Last_name
    
    def is_above_18(self):
        return self.age>18


p1 = Person("Amit","Kushwaha",5)  #create a  class object 

print(p1.full_name())

print(p1.is_above_18())  # calling intance method 



'''
Output:- 
Amit Kushwaha
False
'''