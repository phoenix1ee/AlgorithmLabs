class SignalMonitor:
    def __init__(self,x:str,y:str):
        #a counter of input signal, initialize = 0 
        self.counter = 1
        # the target signal x
        self.x = x
        # the target signal y
        self.y = y
        # the number of matched bits on signal x and the index of next bit
        self.xnext = 0
        # the number of matched bits on signal y and the index of next bit
        self.ynext = 0
        # list of index of bits being matching on signal x
        self.xmatching = list()
        # list of index of bits being matching on signal y
        self.ymatching = list()
        # list of index lists of completely matched bits on signal x
        self.xmatched = list()
        # list of index lists of completely matched bits on signal y
        self.ymatched = list()
        # list of index of signals that are noise.
        self.noise = [[],[]]
        # a flag to indicate if incoming bits are always noise
        self.trailingnoise = False
        # metrics for performance measurement
        self.pushnos = 0
        self.popnos = 0


    def _pop2noise(self,trailing:bool):
        """
        # internal class method to pop all matching signals to noise
        :param trailing: False for non-trailing noise, True for trailing noise
        :return: no return
        """
        i = 1 if trailing else 0
        while len(self.xmatching)>0 and len(self.ymatching)>0:
            if self.xmatching[0] < self.ymatching[0]:
                self.noise[i].append(self.xmatching.pop(0))
                self.pushnos+=1
                self.popnos+=1
            else:
                self.noise[i].append(self.ymatching.pop(0))
                self.pushnos+=1
                self.popnos+=1
        while len(self.xmatching)>0:
                self.noise[i].append(self.xmatching.pop(0))
                self.pushnos+=1
                self.popnos+=1
        while len(self.ymatching)>0:
                self.noise[i].append(self.ymatching.pop(0))
                self.pushnos+=1
                self.popnos+=1
        self.xnext = 0
        self.ynext = 0

    def push(self, c:str):
        """
        # class method to send a single bit to the monitor and trigger the monitor to process
        :param c: the 1 bit char/string input
        :return: no return
        """
        #check if the input is trailing noise
        if self.trailingnoise:
            if len(self.noise)>0:
                self.noise[1].append(self.counter)
                self.pushnos+=1
            else:
                self.noise[1].append([self.counter])
                self.pushnos+=1
        #all cases other than trailing noise
        else:
            #check if the input match any “next” bit of signal .x and .y
                #preceding noise case
                if c != self.x[self.xnext] and c != self.y[self.ynext] \
                and len(self.xmatched) == 0 and len(self.ymatched) == 0:
                    self._pop2noise(False)
                    self.noise[0].append(self.counter)
                    self.pushnos+=1
                #trailing noise detected case
                elif c != self.x[self.xnext] and c != self.y[self.ynext] \
                and (len(self.xmatched) != 0 or len(self.ymatched) != 0):
                    self._pop2noise(True)
                    self.noise[1].append(self.counter)
                    self.trailingnoise = not self.trailingnoise
                    self.pushnos+=1
                #match to x case
                elif (c == self.x[self.xnext] and c != self.y[self.ynext]) \
                or (c == self.x[self.xnext] and c == self.y[self.ynext] and self.xnext>=self.ynext):
                    self.xmatching.append(self.counter)
                    self.pushnos+=1
                    self.xnext+=1
                    if self.xnext == len(self.x):
                        #pop all matching bit to matched
                        self.xmatched.append([])
                        self.pushnos+=1
                        while len(self.xmatching)>0:
                            self.xmatched[-1].append(self.xmatching.pop(0))
                            self.pushnos+=1
                            self.popnos+=1
                        self.xnext = 0
                #match to y case
                elif (c == self.y[self.ynext] and c != self.x[self.xnext]) \
                or (c == self.x[self.xnext] and c == self.y[self.ynext] and self.xnext<self.ynext):
                    self.ymatching.append(self.counter)
                    self.pushnos+=1
                    self.ynext+=1
                    if self.ynext == len(self.y):
                        #pop all matching bit to matched
                        self.ymatched.append([])
                        self.pushnos+=1
                        while len(self.ymatching)>0:
                            self.ymatched[-1].append(self.ymatching.pop(0))
                            self.pushnos+=1
                            self.popnos+=1
                        self.ynext = 0
        self.counter+=1

    def output(self):
        """
        # class method to extract list of index lists of completely matched bits on signals and list of noise
        :return: no return
        """
        outputnoise = list()
        for i in self.noise:
            self.popnos+=len(i)
            outputnoise.append([j for j in i])
        outputx = list()
        for i in self.xmatched:
            self.popnos+=len(i)
            outputx.append([j for j in i])
        outputy = list()
        for i in self.ymatched:
            self.popnos+=len(i)
            outputy.append([j for j in i])
        
        #outputy = [[int(y)+1 for y in yy] for yy in self.ymatched]
        
        self.noise.clear()
        self.xmatched.clear()
        self.ymatched.clear()
        self.counter = 0
        self.xnext = 0
        self.ynext = 0
        self.trailingnoise = False
        pushcount = self.pushnos
        popcount = self.popnos
        self.pushnos = 0
        self.popnos = 0
        return outputnoise, outputx, outputy, pushcount, popcount

# Testing
if __name__ == "__main__":
    test1="100110011001"
    sgm = SignalMonitor("101","010")
    for i in range(len(test1)):
        sgm.push(test1[i])
    noise,x,y,push,pop = sgm.output()
    print(noise,x,y,push,pop)