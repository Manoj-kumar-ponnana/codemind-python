n=int(input())
def near_fibanocii(n):
    if n==0:
        return 0
    f=0
    s=1
    t=f+s
    while t<=n:
        f=s
        s=t
        t=f+s
    if abs(t-n)>abs(n-s):
         print(s)
    elif abs(t-n)==abs(n-s):
        print(s,t)
    else:
        print(t)
near_fibanocii(n)