n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
print("prime") if c==2 else print("not a prime")