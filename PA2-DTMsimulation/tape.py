class cell:
    def __init__(self):
        self.prev = None
        self.v="b"
        self.next = None

class tape:
    """implement an infinite tape"""
    def __init__(self, key=""):
        self.start = cell()
        self.__build__(key)
        self.now = self.start
        
    def __build__(self,key):
        temp = self.start
        for x in key:
            temp.v=x
            temp.next=cell()
            temp.next.prev=temp
            temp=temp.next
    
    def write(self,value):
        self.now.v=value[0]

    def move(self,direction:int):
        if direction>0:
            if not self.now.next:
                self.now.next = cell()   
            self.now = self.now.next
        elif direction<0:
            if not self.now.prev:
                self.now.prev = cell()   
            self.now = self.now.prev
    
    def print(self):
        """print all ever used cell from start"""
        temp = self.start
        s = ""
        while temp and temp.next:
            s = s+temp.v
            temp = temp.next
        return s

# Testing
if __name__ == "__main__":
    test1 = tape("1100")
    test1.move(1)
    test1.move(1)
    test1.move(1)
    #test1.move(1)
    print(test1.now.v)