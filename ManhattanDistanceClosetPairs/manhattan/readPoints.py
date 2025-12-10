from pathlib import Path
import csv

def readPoints(in_path):
    """
    read input file containing lines of coordinates points 
    example line:1,3
    convert and output a list of input data
    :param input_f :a file object which contain some coordinates points
    :return: the list of input data
    """
    points = []
    with open(in_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')  # Change delimiter if needed
        for row in reader:
            if row:
                points.append([int(row[0]),int(row[1])])
    return points
    
# Testing
if __name__ == "__main__":
    inpath = Path('ProgrammingAssignment1\input\whiteBox1.txt')
    print(readPoints(inpath))
    