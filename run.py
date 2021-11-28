from readinput import *
from LNN import *
from random import shuffle,random
from math import ceil
if __name__=="__main__":
    x,y=getdata("mnist_train.csv")
    print("reading done")
    model=MLP(lr=0.05,s=0.1)
    print("model built")
    batch_size=256
    model.train=True
    pre_acc=0
    for _ in range(10):
        shuffle(x)
        for i in range(ceil(len(x)/batch_size)):
            pre_acc=model.update(x[i*batch_size:min((i+1)*batch_size,len(x))],y[i*batch_size:min((i+1)*batch_size,len(x))],pre_acc)
            print(i,pre_acc)
        print('*****************************************************************')
        print('*****************************************************************')
        print('*****************************************************************')
        print('*****************************************************************')
    x,y=getdata("mnist_test.csv")
    test_acc=model.test(x,y)
    print(test_acc)
        
    
