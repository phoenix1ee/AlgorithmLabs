import csv
from pathlib import Path
import argparse

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
    return scalarMul(output,deter)

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='Find Markov Chain state probability: csv file represeting input state matrix')
this_parser.add_argument('n_file', type=str, help="Input File containing the matrix")
this_parser.add_argument('-o', action='store_true', help="Optional, print the operation result to file")
args = this_parser.parse_args()

# Set the input file path
in_path = Path(args.n_file)

if in_path.is_file():
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
    #ending matrix is 2x2:
    if len(temp)==2:
        k2 = 1/(1-temp[1][1])*temp[0][1]
        k.append(k2)
        print(f"k2={k2}")
        output.append(f"k2={k2}")
    """
    for i in range(1,size):
        n = i+1
        temp = 1/(1-Q[n])*vectMul(k,GetCol(W[n],-1))
        k.append(temp)
        print(f"k{n}={temp}")
        output.append(f"k{n}={temp}")
    alpha1 = 0
    for x in k:
        alpha1+=x
    alpha1=1/alpha1
    print(f"alpha1={alpha1}")
    output.append(f"alpha1={alpha1}")
    alpha = [x*alpha1 for x in k]
    alpha2dp = [round(x,3) for x in alpha]
    print("steady state probability with 3 decimal points:")
    print(alpha2dp)
    output.append("steady state probability with 3 decimal points:")
    output.append(alpha2dp)

    #output to file
    if args.o:
        filename = str(in_path.name)
        out_path = str(in_path.absolute())
        out_pathdir = out_path[:len(out_path) - len(filename)]
        out_pathreal = Path(out_pathdir + "output.txt")
        with (out_pathreal.open('w') as file):
            for x in output:
                file.write(str(x))
                file.write("\n")
    """
else:
    raise Exception(f'input file in {in_path.absolute()} do not exist')