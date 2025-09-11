from pathlib import Path


def writeAnalysis(output_f, result):
    """
    write analysis to output file
    example line:inputfilename, data size, m size, processing time(ns)
    :param output_f :a file object for written to
    :param result : the list containing an entry of analysis data
    :return: None
    """
    with (output_f.open('a') as file):
        file.write(result)
        file.write("\n")

    
# Testing
if __name__ == "__main__":
    inpath = Path('ProgrammingAssignment1\input\whiteBox1_output.txt')
    result = "123,testing,1234"
    print(writeAnalysis(inpath,result))
    