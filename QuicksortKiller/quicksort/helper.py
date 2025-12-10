import csv
from pathlib import Path

def numreader(in_path):
    """
    read input file containing lines of values 
    example line:56
    and output a list of input data
    :param input_f :a file object which contain some coordinates points
    :return: the list of input data
        """
    points = []
    with open(in_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row:
                points.append(int(row[0]))
    return points

def writeResults(output_f, result):
    """
    obtain an output file and write the result list to the output file
    example line:1,3
    :param output_f :a file object for written to
    :param result : the list containing the output data
    :return: None
    """
    with (output_f.open('w') as file):
        for x in result:
            file.write(str(x))
            file.write("\n")
    

# Testing
if __name__ == "__main__":
    inpath = Path('..\datafile\PA3whiteBox_rand.txt')
    print(numreader(inpath))