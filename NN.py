from m import *
class linear:
    def __init__(self,Cin,Cout):
        training=True
        self.W=new(Cin,Cout)
        
    def __call__(self,Lin,A=None):
        self.Lin=Lin
        if A:
            temp=ele(self.W,A,'W')
        else:
            temp=sel.W
        self.Lout=mul(Lin,temp)
        return self.Lout[:]
        
    #def backward(self,gin):
    #    mul(gin*self.Lout)
        
    def update(self,A):
        if shape(A)==shape(self.W) , "A+W: "str(shape(A)) + " + " + str(shape(self.W))
        self.W=ele(self.W,A,"+")
        
        
    
