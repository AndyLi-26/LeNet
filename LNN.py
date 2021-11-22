from random import random
from m import *
class MLP:
    def __init__(self,lr,s,d):
        '''
            s: pick s portion of the data during trainning
            d: modify d portion of the weight in the model
            '''
        self.s=s
        self.train=False
        self.lr=lr
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 10)
        
    def forward(self, x, A=None):
        if self.train:
            x = Relu(self.fc1(x))
            x = Relu(self.fc2(x))
            x = Relu(self.fc3(x))
            x = self.fc4(x)
        else:
            x = Relu(self.fc1(x))
            x = Relu(self.fc2(x))
            x = Relu(self.fc3(x))
            x = self.fc4(x)
        return x
        
    def train():
        r,c=shape(self.fc1)
        h=new(r,c)
        for i in range(r):
            for j in range(c):
                if random()<self.d:
                    h[i][j]=random()*self.lr
        self.forward()