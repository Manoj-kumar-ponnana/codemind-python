import math
def strong_number(n):
    s=0
    t=n
    while n>0:
        r=n%10
        s=s+ math.factorial(r)
        n=n//10
    if t==s:
        print("The number {} is a strong number".format(t))
    else:
        print("The number {} is not a strong number".format(t))
n=int(input())
strong_number(n)