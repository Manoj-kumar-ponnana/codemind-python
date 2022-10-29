def add_digit(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n=n//10
    if s//10==0:
        return s
    else:
        return add_digit(s)
a=int(input())
print(add_digit(a))