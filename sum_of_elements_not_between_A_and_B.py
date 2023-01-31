n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
for i in l:
    if i<x or i>y:
        s=s+i
print(s)