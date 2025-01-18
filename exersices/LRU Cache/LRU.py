# class CashNode:
#     def __init__(self,key,value):
#         self.key = key
#         self.value = value
#         self.next = None
#         self.prev = None
#     def __repr__(self):
#         lst = [self.key,self.value]
# class LinkedList:
#     def __init__(self):
#         self.head =None
#         self.tail =None
#         self.len= 0
#     def append(self,Node:CashNode):
        
#         if self.len == 0:
#                 self.head = Node
#                 self.tail = Node
#                 self.head.next = self.tail
#                 self.tail.prev = self.head
#         elif self.len == 1:
#             self.head.next = Node
#             self.tail = Node
#             self.tail.prev = self.head
#         else:
#             self.tail.next = Node
#             self.tail.next.prev = self.tail
#             self.tail = self.tail.next

#     def pop(self):
#         if self.head == None:
#             return "damn"
#         if self.len == 1:
#             key = self.head.key
#             self.head = None
#             self.tail = None
#             return key
#         key = self.head.key
#         self.head = self.head.next
#         self.head.prev = None
#         return key
#     def __repr__(self):
#         lst =[self.head,self.tail]
#         return 
# class LRU_Chash:
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.current = 0
#         self.dict = {}
#         self.LinkedList = LinkedList()

#     def put(self,key,value):
#             if self.current == self.capacity:
#                 del self.dict[self.LinkedList.pop()]
#             try :
#                 self.dict[key].value = value
#                 self.LinkedList.append(self.dict[key])
#                 self.current += 1
#             except:
#                 self.dict[key] = CashNode(key,value)
#                 self.LinkedList.append(self.dict[key])
#                 self.current += 1

#             return "null"
#     def get(self,key):
#         try :
#             node = self.dict[key]
#             value = node.value
#             self.LinkedList.append(self.dict[key])
#             return value
#         except :
#             return -1
# inputList =["LRUCache","put","put","get","put","get","put","get","get","get"]
# commandList =[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# LRU = LRU_Chash(commandList[0][0])
# inputList = inputList[1:]
# commandList = commandList[1:]
# resList = ["null",]
# for i in range(len(inputList)):
#     if inputList[i] == "get":
#         resList.append(LRU.get(commandList[i]))
#     else:
#         resList.append(LRU.put(commandList[i][0],commandList[i][1]))
# print(resList)
class CashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'({self.key}, {self.value})'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append_to_tail(self, node:CashNode):
        if self.len == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.len += 1

    def remove(self, node: CashNode):
        if self.len == 0:
            return
        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.len -= 1

    def pop_head(self):
        if self.len == 0:
            return None
        lru_node = self.head
        self.remove(lru_node)
        return lru_node

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(f'({current.key}, {current.value})')
            current = current.next
        return " <-> ".join(nodes)


class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.linked_list = LinkedList()

    def put(self,key,value):
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.linked_list.remove(node)
            self.linked_list.append_to_tail(node)
        else:
            if self.linked_list.len == self.capacity:
                lru_node = self.linked_list.pop_head()
                del self.dict[lru_node.key]
            new_node = CashNode(key, value)
            self.dict[key] = new_node
            self.linked_list.append_to_tail(new_node)

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.linked_list.remove(node)
            self.linked_list.append_to_tail(node)
            return node.value
        else:
            return -1

    def __repr__(self):
        return f'Cache: {self.dict}\nLinkedList: {self.linked_list}'

commands = input().split()
values = []
for _ in range(len(commands)):
    try:
        values.append(input().strip())
    except EOFError:
        break

output = []
lru = None
value_index = 0
for command in commands:
    if command == "LRUCache":
        capacity = int(values[value_index])
        lru = LRU_Cache(capacity)
        output.append("null")
        value_index += 1
    elif command == "put":
        key, value = map(int, values[value_index].split())
        lru.put(key, value)
        output.append("null")
        value_index += 1
    elif command == "get":
        key = int(values[value_index])
        result = lru.get(key)
        output.append(str(result))
        value_index += 1

print("\n".join(output))
