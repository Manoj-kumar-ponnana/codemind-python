def add_digit(n):
    s=0
    while n>0:
        r=n%10
        s+=r*r
        n=n//10
    if s//10 ==0:
        return s
    else:
        return add_digit(s)
a=int(input())
if add_digit(a) ==1 or add_digit(a)==7:
    print("True")
else:
    print("False")