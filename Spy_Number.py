n=int(input())
s=0
p=1
while n>0:
    r=n%10
    n=n//10
    s+=r
    p*=r
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")