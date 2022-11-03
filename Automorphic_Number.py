n=int(input())
t=n*n
ld=t%(10**len(str(n)))
if ld==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")