# introdction of multiple_inheritance   in python
# mostly developer avoid it because it code complexity increases 

class A :
    def multilevel_a_class ():
        return 'I \' just a class A method '
    
    
    def hello():
        return "Hello form class A "
    
class B:
    def multilevel_b_class ():
        return 'I \' just a class B method '
    
    
    def hello():
        return "Hello form class B"
    
    
class C(A,B):
    pass 

multi = C.multilevel_a_class()
multi2 = C.multilevel_b_class()
print(" the is connected to Class A:",multi)

print("\n  the is connected to Class B:",multi2)

print(C.__mro__)  # method resoulution order of class C 


'''
Output :- 

the is connected to Class A: I ' just a class A method 

the is connected to Class B: I ' just a class B method
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
 '''