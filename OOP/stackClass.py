class Stack:
    def __init__(self):
        self.__length = 0
        self.__isEmpty = True
        self.__storage = []
    @property
    def isEmpty(self):
        return self.__isEmpty
    def peek(self):
        if self.isEmpty:
            return None
        else:
            return self.__storage[-1]
    def push(self,item):
        if self.__length==0:
            self.__isEmpty=False
        self.__storage.append(item)
        self.__length+=1
    def pop(self):
        if self.isEmpty:
            print("Bruh you cant pop an empty stack")
        else:
            self.__storage.pop()
            self.__length-=1
            if self.__length==0:
                self.isEmpty=True
    def __len__(self):
        return self.__length

test = Stack()
print(test.isEmpty)
test.push(4)
test.push(9)
print(test.peek())
test.pop()
print(test.isEmpty)
print(test.peek())
print(len(test))
    