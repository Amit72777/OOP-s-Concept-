''' we introduce multiple  inheritance in this programm '''

class Phone :   # base class / parent class 
    def __init__(self,brand_name,model_name,price ):
        self._brand_name = brand_name
        self._model_name = model_name
        self._price = max(price,0)    # if we pass negatiove value it  replace by zero 

    
    def full_name(self):
        return f"{self._brand_name} {self._model_name}"
    
    def make_a_call(self,Phone_number ):
        return f" Calling the {Phone_number}"
    


class  SmartPhone(Phone):# Child / derive  class 
    def __init__(self,brand_name,model_name,price,ram,internal_memory,rear_camera):
        Phone.__init__(self,brand_name,model_name,price)
        self._RAM = ram
        self._internal_memory = internal_memory
        self.rear_camera  = rear_camera

class FlagshipPhone(SmartPhone):  # child class 
    def __init__(self,brand_name,model_name,price,ram,internal_memory,rear_camera,front_camera,processor = 'Not define '):

        super().__init__(brand_name,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera
        self.processor = processor 






p1 = Phone("nokia","1200",1500)

p2 = SmartPhone("Oppo","A53",13000,"4GB","64GB","48MP")

p3 = FlagshipPhone("Onepluse",'3',40000,'10Gb','256Gb', '64Mp', '48MP', "Snapdragon"  )

print(f'Name of phone {p1.full_name()}  \nFull name of Smart Phone is :- {p2.full_name()} \nPrice of SmartPhone is :- {p2._price}')
# print(FlagshipPhone.__mro__)   # method resolution order 

print("the flagshiipPhone class instance ",p3.full_name())
'''
Output:-

Name of phone nokia 1200  
Full name of Smart Phone is :- Oppo A53 
Price of SmartPhone is :- 13000
the flagshiipPhone class instance  Onepluse 3

'''