
nw = list(map(int,input().split()))
num = list(map(int,input().split()))

n = nw[0]
w = nw[1]

num.sort()



currentWeight = 0
count = 0

for i in range(n):
    if(currentWeight+num[i]>w):
        break
    else:
        currentWeight += num[i]
        count+=1

print(count)
