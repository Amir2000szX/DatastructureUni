from Listing import List
class Node:
    def __init__(self,day,price):
        self.day = day
        self.price = price
        self.SD = None
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,node:Node):
        self.stack.append(node)
        self.top = node
        
    def pop(self):
        if self.top == None:
            raise IndexError
        else:
            self.top = self.stack[-2]
            self.stack.pop()
            
            
def SDFinder(lstDay:List[List]):
    ResStack = Stack()
    for i in range(len(lstDay)):
        NewNode= Node(day=lstDay[i][0],price=lstDay[i][1])
        ResStack.push(NewNode)

