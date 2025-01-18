class Node:
    def __init__(self,value):
        self.value = value
        self.parent = None
        self.leftChild = None
        self.rightChild = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def minimum(self,top=None):
        if top == None:
            top = self.root
        if top.leftChild == None:
            return top
        else:
            return self.minimum(top.leftChild)
        
    def maximum(self,top:Node):
        if top == None:
            top = self.root
        if top.rightChild == None:
            return top
        else:
            return self.maximum(top.rightChild)
    def successor(self,x:Node):
        if self.root == None:
            raise IndexError
        if x.rightChild == None:
            y = x.parent
            while y != None and y.right == x:
                x = y
                y = y.parent
            return y
        else:
            return self.minimum(x.rightChild)

    def predecessor(self,x:Node):
        if self.root == None:
            raise IndexError
        if x.leftChild == None:
            y = x.parent
            while y != None and y.leftChild == x:
                x = y
                y = y.parent
            return y
        else:
            return self.maximum(x.leftChild)
    
    def search(self,value,startNode:Node):
        if startNode == None:
            return False
        if value > startNode.value:
            return self.search(value,startNode.rightChild)

        elif value < startNode.value:
            return self.search(value,startNode.leftChild)
        elif value == startNode.value:
            return True

    def isLeaf(self,node:Node):
        if node.leftChild == None and node.rightChild == None :
            return True
        else :
            return False
    
    def deleteNode(self,value,startNode:Node=None):
        if startNode == None:
            startNode = self.root
        if value > startNode.value:
            self.deleteNode(value,startNode.rightChild)
        elif value < startNode.value:
            self.deleteNode(value,startNode.leftChild)

        elif value == startNode.value:
            if startNode.parent != None:
                y = startNode.parent
                if self.isLeaf(startNode) == True:
                    if y.rightChild.value == value:
                        y.rightChild = None
                    else:
                        y.leftChild = None
                else:
                    successor =self.successor(startNode)
                    successor.leftChild = startNode.leftChild
                    startNode.leftChild.parent = successor
                    
            elif startNode.parent == None:
                if self.root.rightChild == None:
                    self.root = self.root.leftChild
                    self.root.parent = None
                elif self.root.leftChild != None and self.root.rightChild != None:
                     rootsuccessor = self.successor(self.root)
                     self.root = rootsuccessor

                     self.root.leftChild
                     self.root.leftChild.parent =self.root.rightChild

                

            else:
                print("value not found")
            

    def add(self,node:Node):
        if self.root == None:
            self.root == node
        else:
            y = None
            x = self.root
            while(x!=None):
                y = x
                if x.value >= node.value:
                    x = x.leftChild
                else:
                    x = x.rightChild
            x =node
            x.parent = y
            if x.value <= x.parent.value:
                x.parent.leftChild = x
            else:
                x.parent.rightChild = x



        