from random import random
from m import *
from NN import *
class MLP:
    def __init__(self,lr,s):
        '''
            s: pick s portion of the data during trainning
            d: modify d portion of the weight in the model
            '''
        self.s=s
        self.train=False
        self.lr=lr
        self.layer = [linear(784, 512),
        linear(512, 256),
        linear(256, 128),
        linear(128, 10)]
        
    def test(self,x,y):
        rawy=self.forward(x)
        acc=self.acc(rawy,y)
        return acc
        
    def forward(self, x, A=None):
        if A:
            for i,l in enumerate(self.layer[:-1]):
                x=ReLU(l(x,A[i]))
            x=self.layer[-1](x)
        else:
            for i in self.layer[:-1]:
                x=ReLU(i(x))
            x=self.layer[-1](x)
        return x
        
    def acc(self,rawy,y):
        assert len(rawy)==len(y),"rawy has"+str(len(rawy))+"data"+",y has"+str(len(y))+"data"
        correct=0
        for yi,yd in enumerate(rawy):
            ind=yd.index(max(yd))
            if y[yi]==ind:
                correct+=1
        return correct/len(y)
        
    def update(self,x,y,pre_acc):
        assert len(x)==len(y),"x has"+str(len(x))+"data"+",y has"+str(len(y))+"data"
        #pick new step size weight matrix
        H=[]
        for i in range(len(self.layer)):
            r,c=shape(self.layer[i].W)
            h=new(r,c)
            for i in range(r):
                for j in range(c):
                    if random()<self.s: #monte calro
                        h[i][j]=random()*self.lr*0.3-0.15
            H.append(h)
        
        #forward
        rawy=self.forward(x,H)
        #get new acc and update
        new_acc=self.acc(rawy,y)
        if pre_acc>new_acc:
            for i,l in enumerate(self.layer):
                l.update(H[i],"-")
        else:
            for i,l in enumerate(self.layer):
                l.update(H[i],"+")
        # return updated acc
        return self.test(x,y)