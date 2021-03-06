## use numpy do operation
# from math import exp
import numpy as np
def new(r,c):
    return np.zeros((r,c))
    #return [[0 for _ in range(c)] for _ in range(r)]

def dot(a,b):
    assert len(a)==len(b), str(len(a))+'dot'+str(len(b))
    return sum([a[i]*b[i] for i in range(len(a))])

# def shape(A):
#     return len(A),len(A[0])
    
 
    # assert A.shape[1]==B.shape[0],str(A.shape)+" X "+str(B.shape)    
    # C=new(len(A),len(B[0]))
    # for i in range(len(C)):
    #     for j in range(len(C[0])):
    #         C[i][j]=sum([A[i][k]*B[k][j] for k in range(len(A[0]))])
    # return C
    
##def ele(A,B,op):
##    #TODO find sth in numpy to replace this
##    assert len(A)==len(B),str(A.shape)+" X "+str(B.shape)
##    assert len(A[0])==len(B[0]),str(A.shape)+" X "+str(B.shape)
##    assert op in ['+','-','*','/'], "op = "+op
##    C=[]
##    for i in range(len(A)):
##        if op=='*':
##            C.append([A[i][j]*B[i][j] for j in range(len(A[i]))])
##        elif op=='+':
##            C.append([A[i][j]+B[i][j] for j in range(len(A[i]))])
##        elif op=='-':
##            C.append([A[i][j]-B[i][j] for j in range(len(A[i]))])
##        elif op=='/':
##            C.append([A[i][j]/B[i][j] for j in range(len(A[i]))])
##    return C
    
# def T(A):
#     C=new(A[0],A)
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             C[j][i]=A[i][j]
#     return C
    
# def sig(L):
#     assert str(L[0]).isnumeric(), "Layer shape: "+str(shape(L))
#     return list(map(lambda x: 1/(1+math.exp(-x)),L))

def ReLU(L,a=0):
    return np.where(L > 0, L, a*L) 

if __name__=="__main__":
    A=new(256,784)
    B=new(784,512)
    C=mul(A,B)
    
    
    
 
