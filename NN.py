from m import *
class linear:
    def __init__(self,Cin,Cout):
        training=True
        self.W=new(Cin,Cout)
        
    def __call__(self,Lin):
        self.Lin=Lin
        self.Lout=mul(Lin,self.W)
        return self.Lout[:]
        
    def backward(self,gin):
        mul(gin*self.Lout)
        
    
