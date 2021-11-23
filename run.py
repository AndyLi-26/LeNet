if __name__=="__main__":
    x,y=getdata("mnist_train.csv")
    model=MLP(lr=0.1,s=0.1)
    model.train=True
    pre_acc=0
    for _ in range(200):
        pre_acc=update(x,y,pre_acc)
        print(new_acc)
    x,y=getdata("mnist_test.csv")
    test_acc=model.test(x,y)
    print(test_acc)
        
    