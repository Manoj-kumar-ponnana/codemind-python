n=int(input())
l=list(map(int,input().split()))
c=0
z=sum(l)/n
for i in l:
    if i<=z:
        c=c+1
print(c)