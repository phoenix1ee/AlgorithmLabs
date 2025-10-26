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

def printout(sorted: list, comp, exch, output_f, source):
    output_f.write(f'From {source}:'+"\n")
    if len(sorted) <= 50:
        output_f.write("The sorted elements are:"+"\n")
        spacing = 10
        i = 0
        for x in sorted:
            if i == 10:
                output_f.write("\n")
                i = 0
            output_f.write(str(x) + " ")
            i += 1
        output_f.write("\n")
    output_f.write(f'Total no. of sorted elements: {len(sorted)}'+"\n")
    output_f.write(f'Total no. of comparison/exchanges make is {comp} and {exch}'+"\n")

# Testing
if __name__ == "__main__":
    inpath = Path('..\datafile\PA3whiteBox_rand.txt')
    print(numreader(inpath))