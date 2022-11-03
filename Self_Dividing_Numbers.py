def sd(n):
    t=n
    c=1
    while n>0:
        r=n%10
        if r==0:
            c*=0
        elif t%r==0:
            c*=1
        else:
            c*=0
        n=n//10
    return c
l=int(input())
u=int(input())
for i in range(l,u+1):
    if sd(i) ==1:
        print(i,end=' ')