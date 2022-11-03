n=int(input())
rev=0
t=1
if n<0:
    t*=-1
    n*=t
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev*t)