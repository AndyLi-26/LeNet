def getdata(filename):
    fptr=open(filename,'r')
    fptr.readline()
    x,y=[],[] #read as numpy matrix
    for l in fptr:
        data=l.split(',')
        data=list(map(int,data))
        y.append(data[0])
        x.append(data[1:])
    fptr.close()
    return x,y
if __name__=="__main__":
    x,y=getdata("mnist_test.csv")
    
