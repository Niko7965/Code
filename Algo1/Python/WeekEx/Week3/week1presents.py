num = list(map(int,input().split()))

A = num[0]
L = num[1]
O = num[2]

s = ""

if((A<O) & (A<L)):
    s = s+"Anna "

if(L<A):
    s = s+ "Laura "

if((A>O) or (L>O)):
    s = s+"Oscar"

if(s == ""):
    s = "NONE"

print(s)