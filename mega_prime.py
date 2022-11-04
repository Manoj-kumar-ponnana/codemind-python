#mega prime
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
t=n
while t>0:
    r=t%10
    if is_prime(r)==True:
        c+=1
    t=t//10
if is_prime(n)==True and c==len(str(n)):
    print("Mega Prime")
else:
    print("Not Mega Prime")