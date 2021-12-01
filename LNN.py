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
        
    def forward(self, x, H=None,op=''):
        if H:
            for i,l in enumerate(self.layer[:-1]):
                x=ReLU(l(x,H[i],op))
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
        
    def update(self,x,y):
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
        rawy1=self.forward(x,H,'+')
        rawy2=self.forward(x,H,'-')
        #get new acc and update
        new_acc1=self.acc(rawy1,y)
        new_acc2=self.acc(rawy2,y)
        if new_acc1>new_acc2:
            for i,l in enumerate(self.layer):
                l.update(H[i],"+")
                return new_acc1
        else:
            for i,l in enumerate(self.layer):
                l.update(H[i],"-")
                return new_acc2