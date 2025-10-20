import csv
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

def inverse2x2(A:list):
    deter = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    output = [[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]
    return scalarMul(output,1/deter)

# direct run
if __name__ == "__main__":
    in_path = "markovExample.csv"
    output = list()
    temp=readMatrix(in_path)
    size = len(temp)
    print("input matrix is:")
    output.append("input matrix is:")
    mprint(temp)
    for x in temp:
        output.append(x)
    print("Matrix Reduction Process:")
    output.append("Matrix Reduction Process:")
    #reduction
    W = dict()
    R = dict()
    Q = dict()
    while len(temp)>2:
        r = len(temp)
        W.update({r:partition(temp,0,-2,-2,None)})
        R.update({r:partition(temp,-2,None,0,-2)})
        Q.update({r:partition(temp,-2,None,-2,None)})
        T = partition(temp,0,-2,0,-2)
        IQ = inverse2x2(msub(Imatrix(2),Q[r]))
        temp = madd(mmul(mmul(W[r],IQ),R[r]),T)
        print(f"P{len(temp)}:")
        output.append(f"P{len(temp)}:")
        mprint(temp)
        for x in temp:
            output.append(x)
    
    #enlargement
    print("matrix enlargement: ")
    output.append("matrix enlargement: ")
    k = [1]
    #set next k
    nextk = 3
    #ending matrix is 2x2:
    if len(temp)==2:
        k2 = 1/(1-temp[1][1])*temp[0][1]
        k.append(k2)
        print(f"k2={k2}")
        output.append(f"k2={k2}")
        print(k)
        nextk +=1

    for n in range(nextk,size+1,2):
        kr = mmul(mmul([k],W[n]),inverse2x2(msub(Imatrix(2),Q[n])))
        for x in kr[0]:
            k.append(x)
        print(f"k:{k}")

    