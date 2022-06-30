
class unionFind:

    def __init__(self,n):
        self.n = n
        self.id = [None]*n
        
        for i in range(n):
            self.id[i] = i
            


   

    def find(self,i):
        return self.id[i]

    def union(self,i,j):
        i_id = self.find(i)
        j_id = self.find(j)
        if(i_id != j_id):
            for k in range(self.n):
                if(self.id[k] == i_id):
                    self.id[k] = j_id

n = int(input())
m = int(input())

p = unionFind(n)

for _ in range(m):
    inpLine = input().split()
    if(inpLine[0] =="F"):
        print(p.find(int(inpLine[1])))
    if(inpLine[0] == "U"):
        p.union(int(inpLine[1]),int(inpLine[2]))