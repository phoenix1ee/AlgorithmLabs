from pathlib import Path
import csv

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

# Testing
if __name__ == "__main__":
    inpath = Path('Markov/matrix1.txt')
    temp=readMatrix(inpath)
    for x in temp:
        print(x)
    print(vectMul(temp[0],temp[1]))