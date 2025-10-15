from matrixClass import matrix
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

def madd(A:matrix,B:matrix):
    product = list()
    if A.col == B.row:
        for i in range(A.row):
            product.append([])
            for j in range(B.col):
                product[i].append(A.matrix[i][j]+B.matrix[i][j])
        return matrix(product)
    else:
        raise Exception(f' matrix dimension mismatch when doing multiplication')

def msub(A:matrix,B:matrix):
    product = list()
    if A.col == B.row:
        for i in range(A.row):
            product.append([])
            for j in range(B.col):
                product[i].append(A.matrix[i][j]-B.matrix[i][j])
        return matrix(product)
    else:
        raise Exception(f' matrix dimension mismatch when doing multiplication')

def scalarMul(A:matrix,k=float):
    product = list()
    for i in range(A.row):
        for j in range(A.col):
            product[i].append(A.matrix[i][j]*k)
    return matrix(product)

def mmul(A:matrix,B:matrix):
    """
    read 2 input matrix object
    and return matrix multiplication product
    :param A: input matrix A
    :param B: input matrix B
    :return: a matrix product
    """
    product = list()
    if A.col == B.row:
        for i in range(A.row):
            product.append([])
            for j in range(B.col):
                product[i].append(vectMul(A.matrix[i],B.GetCol(j)))
        return matrix(product)
    else:
        raise Exception(f' matrix dimension mismatch when doing multiplication')

def partition(A:matrix, k:int):
    """
    read matrix object, a range, denoted by k
    and return the partitioned matrix (k*k)
    :param A: input matrix A
    :param k: range needed, 0->till k 
    :return: a matrix product
    """
    output = list()
    for i in range(k):
        output.append([])
        for j in range(k):
            output[i].append(A.matrix[i][j])
    return matrix(output)

# Testing
if __name__ == "__main__":
    test = list()
    test.append([1.1, 2.3, 3.4])
    test.append([4.0, 5.0, 6.7])
    test.append([7.7, 8.8, 9.9])
    temp = matrix(test)
    temp.mprint()
    #print("row1xrow3")
    #print(vectMul(temp[0],temp[2]))
    #Idm = Imatrix(3)
    #for x in Idm:
    #    print(x)
    #product = mmul(matrix(temp),matrix(temp2))
    new = partition(temp,2)
    new.mprint()