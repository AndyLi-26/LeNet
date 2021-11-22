if __name__=="__main__":
    x,y=getdata("mnist_train.csv")
    model=MLP(lr=0.1,s=0.1)
    
    