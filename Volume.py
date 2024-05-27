'''
    program to calculate value of a box  
'''

class Demo:
    
    def __init__(self):
        print("Calling parent constructor")
        
    'set functions'    
    def setPara(self,l,b,h):
        self.l = l;
        self.b = b;
        self.h = h;
        
    'get values from functions'    
    def getPara(self):
        print(self.l)
        print(self.b)
        print(self.h)
        return (self.l*self.b*self.h)
        
    def calValue(self):
        return self.l*self.b*self.h
        

'main function starting here'        
        
obj1 = Demo();
obj1.setPara(4,3,3);
print("Value of box = ",obj1.calValue())


        

