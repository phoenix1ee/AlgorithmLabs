class matrix:
    def __init__(self, m = list):
        self.matrix = m
        self.row = len(m)
        self.col = len(m[0])

    def GetCol(self, col: int):
        output = list()
        for x in self.matrix:
            output.append(x[col])
        return output


    def mprint(self):
        for x in self.matrix:
            print(x)


# Testing
if __name__ == "__main__":
    test = list()
    test.append([1.1, 2.3, 3.4])
    test.append([4.0, 5.0, 6.7])
    test.append([7.7, 8.8, 9.9])
    testm = matrix(test)
    testm.mprint()
    print(testm.Col(2))