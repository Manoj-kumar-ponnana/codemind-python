n=int(input())
c=len(str(n))
s=0
t=n
while n>0:
    r=n%10
    s+=r**c
    c-=1
    n//=10
if s==t:
    print("True")
else:
    print("False")