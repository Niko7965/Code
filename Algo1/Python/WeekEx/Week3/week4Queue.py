from email import header


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    #add to tail
    def enqueue(self,i):
        if self.tail is None:
            self.tail = Node(i)
        else:
            new_node = Node(i)
            self.tail.next = new_node
            self.tail = new_node
        if self.head is None:
            self.head = self.tail
        

    
    #remove head
    def dequeue(self):
        if(self.head is None):
            pass
        else:
            toReturn = self.head.key
            self.head = self.head.next
            return toReturn

    def is_empty(self):
        if(self.head is None):
            return True

class Node():

    def __init__(self,key):
        self.key = key
        self.next = None

n = int(input())

q = Queue()

for _ in range(n):
    inpLine = input().split()

    if(inpLine[0] == "E"):
        q.enqueue(int(inpLine[1]))
       
    if(inpLine[0] == "D"):
        print(q.dequeue())