#nearest prime
t=int(input())
for _ in range(t):
    def is_prime(n):
        if n <2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    def next_prime(n,x):
        while is_prime(n)==False:
            n+=x
        return n
    n=int(input())
    np=next_prime(n,1)
    pp=next_prime(n,-1)
    if np-n<n-pp:
        print(np)
    else:
        print(pp)