m=int(input())
for i in range(m):
    n=int(input())
    a=n
    while True:
        p=True
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                p=False
                break
        if p==True:
            break
        else:
            a+=1
    b=n
    while True:
        p=True
        for i in range(2,int(b**0.5)+1):
            if b%i==0:
                p=False
                break
        if p==True:
            break
        else:
            b-=1
    if a-n < n-b:
        print(a)
    else:
        print(b)