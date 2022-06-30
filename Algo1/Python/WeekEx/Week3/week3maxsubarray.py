

def subsize(b,B,start,end):
    return B[end]-B[start]+b[start]

#First we read the input

n = int(input())

a = [0]*n
A = [0]*n

inpLine = input().split()



for i in range(n):
    a[i] = int(inpLine[i])

    if(i == 0):
        A[i] = a[i]
    else:
        A[i] = A[i-1]+a[i]


max = a[0]

for i in range(n):
    for j in range(i,n):
        if(subsize(a,A,i,j)>max):
            max = subsize(a,A,i,j)


print(max)


