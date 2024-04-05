'''
Create a laptop classs with attributes like brand name , model name, price 

Create  two object/intance of your laptop class

'''

class Laptop :
    discount_persent = 10  # class variable
    def __init__(self,brand_name, model_name,price  ):  # atributes 
        self.brand = brand_name  # Instence 
        self.model = model_name
        self.price = price 
        self.Laptop_name = brand_name +  " " + model_name 

    def discount(self):   # class method 
        return  self.price * (100 - self.discount_persent) / 100 
    
hp = Laptop('Hp', "15eq" , 45000)  # creat object 
p2 = Laptop("apple","3k34ci",90000)
print("\nbrand_name:- ", hp.brand,"\nmodel name :-", hp.model, "\nprice of laptop is :- ", hp.price )
p2.discount_persent = 30 
print("\nLaptop name :- ", p2.Laptop_name,p2.discount())

print("\nafter apply discount  the current price is :- ", hp.discount())   # find discout of laptop 

print(hp.__dict__)

print(p2.__dict__) 
