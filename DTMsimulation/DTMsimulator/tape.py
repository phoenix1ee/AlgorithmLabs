class cell:
    def __init__(self):
        self.prev = None
        self.v="b"
        self.next = None

class tape:
    """implement an infinite tape"""
    def __init__(self, key=""):
        self.start = cell()
        self.start.v = "S"
        self.start.next = cell()
        self.start.next.prev = self.start
        self.__build__(key)
        self.now = self.start
        
    def __build__(self,key):
        temp = self.start.next
        for x in key:
            temp.v=x
            temp.next=cell()
            temp.next.prev=temp
            temp=temp.next
        temp.v="E"
    
    def write(self,value):
        self.now.v=value[0]

    def move(self,direction:int):
        if direction>0:
            if not self.now.next:
                self.now.next = cell()
                self.now.next.prev = self.now
            self.now = self.now.next
        elif direction<0:
            if not self.now.prev:
                self.now.prev = cell()
                self.now.prev.next = self.now
                self.start=self.now.prev
            self.now = self.now.prev
    
    def print(self):
        """return all ever used cell from start S to end as string"""
        temp = self.start.next
        #temp = self.start
        s = ""
        while temp and temp.next:
            if temp != self.now:
                s = s+temp.v
            else:
                s = s+"["+temp.v+"]"
            temp = temp.next
        if not self.now.next:
            s = s+"[_]"
        return s

# Testing
if __name__ == "__main__":
    test1 = tape("1110")
    print(test1.now.prev)
    test1.move(-1)
    print(test1.now.v)
    test1.move(-1)
    print(test1.print())