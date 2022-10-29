def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def sq(n):
    return n*n
n=int(input())
if sq(n)==reverse(sq(reverse(n))):
    print("True")
else:
    print("False")