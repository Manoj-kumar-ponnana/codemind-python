def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if n<2:
    print("-1")
elif n%2==0:
    x=n//2
    if is_prime(x):
        print(2,x)
    else:
        print("-1")
elif n%3==0:
    x=n//3
    if is_prime(x):
        print(3,x)
    else:
        print("-1")
elif n%5==0:
        x=n//5
        if is_prime(x):
            print(5,x)
        else:
            print("-1")
elif n%7==0:
        x=n//7
        if is_prime(x):
            print(7,x)
        else:
            print("-1")
else:
    print("-1")