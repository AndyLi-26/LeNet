from m import *
class linear:
    def __init__(self,Cin,Cout):
        training=True
        self.W=new(Cin,Cout)
    def __call__(self,Lin):
        return mul(Lin,self.W)
    def backward(self):
        pass
    
