from readinput import *
from LNN import *
from random import shuffle,random
from math import ceil
import numpy 
if __name__=="__main__":    

    def shuffle_in_unison(a, b):
        assert len(a) == len(b)
        shuffled_a = numpy.empty(a.shape, dtype=a.dtype)
        shuffled_b = numpy.empty(b.shape, dtype=b.dtype)
        permutation = numpy.random.permutation(len(a))
        for old_index, new_index in enumerate(permutation):
            shuffled_a[new_index] = a[old_index]
            shuffled_b[new_index] = b[old_index]
        return shuffled_a, shuffled_b


    x,y=getdata("mnist_train.csv") 
    print("reading done")
    model=MLP(lr=0.05,s=0.01)
    print("model built")
    batch_size=256
    model.train=True
    for _ in range(10):
        # shuffle(x) ## TODO: shuffle x and y together

        x,y = shuffle_in_unison(x,y)
        for i in range(ceil(len(x)/batch_size)):
            pre_acc=model.update(x[i*batch_size:min((i+1)*batch_size,len(x))],y[i*batch_size:min((i+1)*batch_size,len(x))])
            print(i,pre_acc)
        print('*****************************************************************')
        print('*****************************************************************')
        print('*****************************************************************')
        print('*****************************************************************')
    x,y=getdata("mnist_test.csv")
    test_acc=model.test(x,y)
    print(test_acc)
        
