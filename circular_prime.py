def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
if is_prime(n) and is_prime(reverse(n)):
    print("circular prime")
elif is_prime(n) and is_prime(reverse(n))==False:
    print("prime but not a circular prime")
else:
    print("not prime")