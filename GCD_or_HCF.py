def gcd(n,m):
    if a>b:
        t=b
    else:
        t=a
    for i in range(1,t+1):
        if n%i==0 and m%i==0:
            gcd=i
    return gcd
a,b=map(int,input().split())
print(gcd(a,b))