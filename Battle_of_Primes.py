def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def next_prime(n):
    n+=1
    while is_prime(n)==False:
        n+=1
    return n
a=int(input())
b=int(input())
s=a+b
res=next_prime(s)-s
print(res)