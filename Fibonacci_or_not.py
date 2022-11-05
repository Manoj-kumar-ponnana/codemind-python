n=int(input())
lst=[]
f=0
s=1
t=f+s
for i in range(n):
    lst.append(f)
    f=s
    s=t
    t=f+s
if n in lst:
    print("True")
else:
    print("False")