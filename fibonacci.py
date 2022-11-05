n=int(input())
f=0
s=1
t=f+s
for i in range(n):
    print(f,end=" ")
    f=s
    s=t
    t=f+s