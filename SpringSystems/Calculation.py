import numpy as np

class Calculation: 
    def __init__(self,m,k,b,x0,xv0):
        self.m = m
        self.k = k
        self.b = b 
        self.x0 = x0
        self.xv0 = xv0
        d = ((self.b)**2) - (4*(self.m)*(self.k))
        if d > 0:
            self.classification = "Overdamped"
        elif d == 0:
            self.classification = "Critically damped"
        else:
            self.classification = "Underdamped"
    
    
        
        
        
        
        
        


