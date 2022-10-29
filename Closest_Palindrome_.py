def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def next_palindrome(n,x):
    n+=x
    while n!=reverse(n):
        n+=x
    return n
num=int(input())
np=next_palindrome(num,1)
pp=next_palindrome(num,-1)
if np-num< num-pp :
    print(np)
elif np-num == num-pp :
    print(pp,np)
else:
    print(pp)