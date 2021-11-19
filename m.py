def new(r,c):
    return [[0 for _ in range(c)] for _ in range(r)]

def dot(a,b):
    assert len(a)==len(b), str(len(a))+'dot'+str(len(b))
    return sum([a[i]*b[i] for i in range(len(a)])

def shape(A):
    return len(A),len(A[0])
    
def mul(A,B):
    assert len(A[0])==len(B),str(shape(A))+" X "+str(shape(B))
    C=new(len(A),len(B[0]))
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j]=sum([A[i][k]*B[k][j] for k in range(len(A[0])])
    return C
    
def ele(A,B,op):
    assert len(A)==len(B),str(shape(A))+" X "+str(shape(B))
    assert len(A[0])==len(B[0]),str(shape(A))+" X "+str(shape(B))
    assert op in ['+','-','*','/'], "op = "+op
    C=[]
    for i in range(len(A)):
        if op=='*':
            C.append([A[i][j]*B[i][j] for j in range(len(A[i]))])
        elif op=='+':
            C.append([A[i][j]+B[i][j] for j in range(len(A[i]))])
        elif op=='-':
            C.append([A[i][j]-B[i][j] for j in range(len(A[i]))])
        elif op=='/':
            C.append([A[i][j]/B[i][j] for j in range(len(A[i]))])
    return C
    
def T(A):
    C=new(A[0],A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[j][i]=A[i][j]
    return C
    

def ReLU(L,a=0):
    assert str(L[0]).isnumeric(), "Layer shape: "+str(shape(L))
    O=[]
    for i in L:
        if i>0:
            O.append(i)
        else:
            O.append(a*i)
    return O
    