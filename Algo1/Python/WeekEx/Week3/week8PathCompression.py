




class unionFind:


    def __init__(self,n):
        self.p = [0]*n
        self.sz = [1]*n
        for i in range(n):
            self.p[i] = i
            
   

    def find(self,i):
        visited = []

        while(i != self.p[i]):
            visited.append(i)
            i = self.p[i]
        for k in range(len(visited)):
            visited[k] = i

        return i



    def union(self,i,j):
        rep_i = self.find(i)
        rep_j = self.find(j)
        if(rep_i != rep_j):

            if(self.sz[rep_i]<self.sz[rep_j]):
                self.p[rep_i] = rep_j
                self.sz[rep_j] +=self.sz[rep_i]
            else:
                self.p[rep_j] = rep_i
                self.sz[rep_i] +=self.sz[rep_j]


n = int(input())
m = int(input())

u = unionFind(n)

for _ in range(m):
    inpLine = input().split()
    if(inpLine[0] =="F"):
        print(u.find(int(inpLine[1])))
    if(inpLine[0] == "U"):
        u.union(int(inpLine[1]),int(inpLine[2]))