n=int(input())
l=list(map(int,input().split()))
x,y=list(map(int,input().split()))
z=[]
c=0
for i in l:
    if i<x or i>y:
        z.append(i)
        c=c+1
if c!=0:
    print(max(z))
else:
    print("-1")