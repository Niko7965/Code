




def init(n):
    p = [0]*n
    

    for i in range(n):
        p[i] = i
    return p

def find(p,i):
    while(i != p[i]):
        i = p[i]
    return i

def union(p,i,j):
    rep_i = find(p,i)
    rep_j = find(p,j)
    if(rep_i != rep_j):
        p[rep_i] = rep_j


n = int(input())
m = int(input())

p = init(n)

for _ in range(m):
    inpLine = input().split()
    if(inpLine[0] =="F"):
        print(find(p,int(inpLine[1])))
    if(inpLine[0] == "U"):
        union(p,int(inpLine[1]),int(inpLine[2]))