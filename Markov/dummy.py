import csv
import copy
from pathlib import Path

def readMatrix(in_path):
    """
    read input matrix in csv format
    example line1: 1,2,3
    example line2: 4,5,6
    example line3: 7,8,9
    convert and output a 2-D list, matrix[[row],[row]...]
    :param in_path :a file object which contain DTM table
    :return: the list of input matrix
    """
    Matrix = list()
    with open(in_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')  # Change delimiter if needed
        #print(reader.fieldnames)
        #x=1
        for row in reader:
            for i in range(len(row)):
                row[i] = float(row[i])
            Matrix.append(row)
    return Matrix

def GetCol(m:list, col: int):
    return [x[col] for x in m]

def mprint(m:list):
    for x in m:
        print(x)

def vectMul(A:list,B:list):
    sum = 0
    for i in range(len(A)):
        sum += A[i]*B[i]
    return sum

def Imatrix(size:int):
    I = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        I[i][i]=1
    return I

def madd(A:list,B:list):
    sum = list()
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            sum.append([A[i][j]+B[i][j] for j in range(len(B[0]))])
        return sum
    else:
        raise Exception(f' matrix dimension mismatch when doing multiplication')

def msub(A:list,B:list):
    sum = list()
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            sum.append([A[i][j]-B[i][j] for j in range(len(B[0]))])
        return sum
    else:
        raise Exception(f' matrix dimension mismatch when doing multiplication')

def scalarMul(A:list,k=float):
    product = list()
    for i in range(len(A)):
        product.append([A[i][j]*k for j in range(len(A[0]))])
    return product

def mmul(A:list,B:list):
    """
    read 2 input matrix list
    and return matrix multiplication product A*B
    :param A: input matrix A
    :param B: input matrix B
    :return: a matrix product
    """
    product = list()
    if len(A[0]) == len(B):
        for i in range(len(A)):
            product.append([vectMul(A[i],GetCol(B,j)) for j in range(len(B[0]))])
        return product
    else:
        raise Exception(f' matrix dimension mismatch when doing multiplication')

def partition(A:list, i:int, ii:int, j:int, jj:int):
    """
    read matrix list, 2 ranges, denoted by i:ii and j:jj
    and return the partitioned matrix A with row i to row ii
    and column j to jj 
    :param A: input matrix A
    :param i: starting row
    :param ii: end row
    :param j: starting col
    :param jj: end col
    :return: a matrix list
    """
    return([x[slice(j,jj)] for x in A[slice(i,ii)]])

# Testing
if __name__ == "__main__":
    inpath = Path('markovExample.csv')
    #inpath = Path('matrix1.txt')
    temp=readMatrix(inpath)
    size = len(temp)
    mprint(temp)
    print()
    temp2 = copy.deepcopy(temp)
    """
    test = list()
    test.append([1.1, 2.3, 3.4])
    test.append([4.0, 5.0, 6.7])
    test.append([7.7, 8.8, 9.9])
    test2 = test.copy()
    mprint(test)
    print()
    print(GetCol(test,2))
    print()
    print(vectMul(test[0],GetCol(test,2)))
    print()
    mprint(Imatrix(3))
    print()
    mprint(mmul(test,test2))
    print()
    mprint(madd(test,test2))
    print()
    mprint(msub(test,test2))
    print()
    mprint(scalarMul(test,2))
    print()
    mprint(partition(test2,1,2,1,2))
    """
    #reduction
    W = dict()
    R = dict()
    Q = dict()
    while len(temp)>2:
        W.update({len(temp):partition(temp,0,-1,-1,None)})
        R.update({len(temp):partition(temp,-1,None,0,-1)})
        Q.update({len(temp):temp[-1][-1]})
        T = partition(temp,0,-1,0,-1)
        print(W)
        print(R)
        print(Q)
        IQ = 1/(1-Q[len(temp)])
        temp = madd(mmul(scalarMul(W[len(temp)],IQ),R[len(temp)]),T)
    mprint(temp)
    #enlargement

    k = [1]
    for i in range(2,size+1):
        print(i)