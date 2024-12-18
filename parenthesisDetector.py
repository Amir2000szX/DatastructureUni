
class Stack:
    def __init__(self):
        self.stack = []
        self.top = None

    def push(self,node:str):
        self.stack.append(node)
        self.top = node
        
    def popS(self):
        if self.top == None:
            raise ValueError
        elif len(self.stack) == 1:
            self.top = None
            self.stack.pop()
        else:
            self.top = self.stack[-2]
            self.stack.pop()
    def __len__(self):
        return len(self.stack)
def detect(str:str):
    newStack = Stack()
    
    for i in str:
        if i not in "(){}[]":
            return ValueError
        if i == "(" or i == "{" or i == "[":
            newStack.push(i)
        else:
            if newStack.top == None:
                return 0
            elif newStack.top == "{" and i != "}":
                return 0
            elif newStack.top == "[" and i != "]":
                return 0
            elif newStack.top == "(" and i != ")":
                return 0
            else:
                newStack.popS()
    if len(newStack.stack) == 0:
         return 1
    else:
        return 0
        
str1 = input()
print(detect(str1))