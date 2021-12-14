from m import *
class linear:
    def __init__(self,Cin,Cout):
        training=True
        self.W=new(Cin,Cout)
        
    def __call__(self,Lin,h=None,op=''):
        if not h is None:
            return np.matmul(Lin,self.W+h if op else self.W-h)
        else:
            return np.matmul(Lin,self.W)

    def update(self,A):
        # assert A.shape==self.W.shape, "A+W: "+str(A.shape) + " + " + str(self.W.shape)
        self.W=self.W+A
    
