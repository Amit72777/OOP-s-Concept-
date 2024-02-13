''' using class method we are  create a constructor to take all attributes in a single string  '''

class Person:
    No_instan = 0 
    def __init__(self,First_name ,Last_name,age = None , gender = None ):
        '''the intatance of a class  '''
        self.First_name = First_name
        self.Last_name = Last_name
        self.Full_name = First_name + " " +  Last_name
        self.age = age 
        self.Sex = gender 
        Person.No_instan += 1 

    @classmethod
    def form_string(cls,str):  # first argument take by default class 
        first,last,age1,gend = str.split(",")
        return cls(first,last,int(age1),gend)   # convert age data type 
    
    def is_above_18(self):  # check  person is above 18 or not and & self take  object as a argument by default 
        return 18<self.age

# count how any object  has been created 
    @classmethod
    def count_intstance(cls):   # by default cls argument take class 
        return Person.No_instan
    

p1 = Person("Amit","Kushwaha", 18,"Male")
p2 = Person("Utkarsh","Dwivedi", 20,"Male")

p3 = Person.form_string("Rahul,Kushwaha,39,'female'")

print(f"ther are {Person.count_intstance()} instance in {Person.__name__}",Person.count_intstance())

print(  p3.is_above_18()  )