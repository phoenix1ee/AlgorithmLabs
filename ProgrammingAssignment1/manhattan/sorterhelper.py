class nmnode:
    def __init__(self, in_v: int):
        """
        This class is used to hold a linked list of elements
        """
        self.v = in_v
        self.next = None

def convert(node1: nmnode):
    current = node1
    nums = []
    while current:
        nums.append(current.v)
        current = current.next
    return nums

def numreader(input_f, sorttype='others'):
    """
        Read from the input file object and Output an array of numbers, or an array of lists of numbers
        ignoring all spaces and escape character "\t"
        :argument: in_path :a file object which contain some expression
        :return: an array, an array of error line, no. of comparisons and exchange make
        """
    nums = []
    error = []
    line = 0
    newlist = True
    cp = 0
    ex = 0
    for l in input_f:
        line += 1
        in_c = l.strip().replace(" ", "")
        if in_c and in_c.isnumeric():
            if sorttype != 'nmgl':
                nums.append(int(in_c))
            else:
                if newlist:
                    temp = nmnode(int(in_c))
                    newlist = False
                    current = temp
                else:
                    cp += 1
                    if int(in_c) >= current.v:
                        current.next = nmnode(int(in_c))
                        current = current.next
                    else:
                        nums.append(temp)
                        temp = nmnode(int(in_c))
                        current = temp
        else:
            if len(in_c) == 0:
                error.append((line, "empty line"))
            else:
                error.append((line, "invalid line"))
    if sorttype == 'nmgl' and temp:
        nums.append(temp)
    return nums, error, cp, ex

from sorter.qsort1st import qsort1st
from sorter.qsort10 import qsort10
from sorter.qsort50 import qsort50
from sorter.qsort100 import qsort100
from sorter.qsortmo3 import qsortmo3
from sorter.mergesrt import mergesrt
from sorter.nmglinked import nmglinked

def sortthisway(input_f, sorttype, path):
    """
    The entry point for the quicksort module, it creates the list by reading from the input file object
    then sort it according to the user preference of sort strategy
    :param input_f :a file object which contain some numbers
    :param sorttype :the user input of sorting strategy
    :param path :the file path of input file
    :return: the list, no. of comparisons and exchange make
    """
    sortbook = {'q1': qsort1st, 'q10': qsort10, 'q50': qsort50, 'q100': qsort100, 'mo3': qsortmo3, 'mg':mergesrt, 'nmgl':nmglinked}
    numbers, invalidline, cps, exs = numreader(input_f, sorttype)
    for x1 in invalidline:
        print(f'{x1[1]} detected in line{x1[0]} in {path}')
    if len(numbers) == 0:
        print(f'{path} contain no valid line')
        return numbers, cps, exs
    else:
        if sorttype in ['q1','q10','q50','q100','mo3']:
            numbers, temp_cps, temp_exs = sortbook[sorttype](numbers, 0, len(numbers) - 1)
            cps += temp_cps
            exs += temp_exs
        elif sorttype in ['mg']:
            numbers, temp_cps, temp_exs = sortbook[sorttype](numbers)
            cps += temp_cps
            exs += temp_exs
        elif sorttype in ['nmgl']:
            tempnode, temp_cps, temp_exs = sortbook[sorttype](numbers)
            numbers = convert(tempnode)
            cps += temp_cps
            exs += temp_exs
    return numbers, cps, exs

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