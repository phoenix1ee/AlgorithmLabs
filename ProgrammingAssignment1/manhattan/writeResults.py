from pathlib import Path

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
    testwrite=[[[1, 2], [1, 3]], [[1, 2], [3, 1]], [[1, 3], [3, 1]], [[1, 3], [4, 4]]]
    outpath = Path('ProgrammingAssignment1\datafile\output_testwrite.txt')
    writeResults(outpath,testwrite)
    
