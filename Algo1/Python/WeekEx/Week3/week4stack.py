

class Node():
    
    
    def __init__(self,key):
        self.key = key
        self.next = None
    



class Stack():

    def __init__(self):
        self.head = None
    
    def push(self,i):
        if self.head is None:
            self.head = Node(i)
        else:
            newNode = Node(i)
            newNode.next = self.head
            self.head = newNode
        
    
    def pop(self):
       
        if self.head is None:
            return None
        else:
            toReturn = self.head.key
            self.head = self.head.next
            return toReturn





    





n = int(input())

s = Stack()

for _ in range(n):
    inpLine = input().split()

    if(inpLine[0] == "PU"):
        s.push(int(inpLine[1]))
       
    if(inpLine[0] == "PO"):
        print(s.pop())