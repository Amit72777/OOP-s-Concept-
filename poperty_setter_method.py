#we focus of set by default value if we enter (-ve) price it will automatic change into  0 

class Phone:
    def __init__(self,brand,model,price):
        self._brand = brand                 # use single '_'   for private instance method 
        self.__model_name = model            #use name Mangling 
        self._price = max(price,0)                      # Use max() when we enter -numbere it will set by default zero 

    def make_a_call(self,phone_number ):
        print(f"calling the {phone_number}")

    def Full_name(self):
        return f"{self.brand} {self.__model_name}"
    
    @property    # Property  allows you to access the attribute as if it were a property, without directly calling a method.
    def complete_specification(self):
        return f"{self._brand} {self.__model_name}  and the price is {self._price}"
    
    @property
    def price(self):
        return self._price
    
    @price.setter    # It allows you to set the value of the property as if it were a property, without directly calling a method.
    def price(self,new_price):
        self._price  = max(new_price,0)    

phn1 = Phone("oppo","A53",1100)
print(phn1.complete_specification)

print(phn1.__dict__)  # .__dict__ return the dictionary for all attributes of object 

# change a price 
phn1.price  = -600   # we use new name price of change a number  if  we use original attributes _price we face a problem 


print(" Price of phone is :- ", phn1._price )    
print(phn1.complete_specification)
print(phn1.price)
