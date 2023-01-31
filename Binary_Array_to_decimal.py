n=int(input())
l=list(map(int,input().split()))
l.reverse()
c=0
x=0
for i in l:
    if i==1:
        c=c+(2**x)
    x=x+1
print(c)