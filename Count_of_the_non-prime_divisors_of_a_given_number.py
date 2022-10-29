def is_prime(n):
    if n <2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def divisors_count(n):
    c=0
    for i in range(1,n+1):
        if is_prime(i)==False and n%i==0:
            c+=1
    return c
n=int(input())
print(divisors_count(n))