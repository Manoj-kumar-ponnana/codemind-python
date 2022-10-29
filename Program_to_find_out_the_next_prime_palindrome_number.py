def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def rev(n):
    r=0
    while n>0:
        t=n%10
        r=r*10+t
        n=n//10
    return r
a=int(input())
a+=1
while 1:
    if rev(a)==a and prime(a)== True:
        print(a)
        break
    a+=1