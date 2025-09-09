def readPoints(input_f):
    """
    read input file containing lines of coordinates points 
    example line:1,3
    convert and output a list of input data
    :param input_f :a file object which contain some coordinates points
    :return: the list of input data
    """
    points = []
    error = []
    line = 0
    for l in input_f:
        line += 1
        in_c = l.strip().replace(" ", "")
        if in_c and in_c.isnumeric():
            pass
        else:
            if len(in_c) == 0:
                error.append((line, "empty line"))
            else:
                error.append((line, "invalid line"))
    return points, error
    
test="1,34"

