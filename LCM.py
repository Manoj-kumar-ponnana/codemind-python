a,b=map(int,input().split())
g=max(a,b)
while 1:
    if g%a==0 and g%b==0:
        print(g)
        break
    g+=1
    