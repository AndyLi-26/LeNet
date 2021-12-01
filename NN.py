from m import *
class linear:
    def __init__(self,Cin,Cout):
        training=True
        self.W=new(Cin,Cout)
        
    def __call__(self,Lin,h=None,op=''):
        self.Lin=Lin
        if h:
            temp=ele(self.W,h,op)
        else:
            temp=self.W
        self.Lout=mul(Lin,temp)
        return self.Lout
        
    #def backward(self,gin):
    #    mul(gin*self.Lout)
        
    def update(self,A,op):
        assert shape(A)==shape(self.W), "A+W: "+str(shape(A)) + " + " + str(shape(self.W))
        self.W=ele(self.W,A,op)
        
        
    
