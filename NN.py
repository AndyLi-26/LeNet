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
                
    def update(self,A,op):
        # assert A.shape==self.W.shape, "A+W: "+str(A.shape) + " + " + str(self.W.shape)
        self.W=ele(self.W,A,op)
    
