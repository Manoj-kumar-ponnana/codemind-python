n=int(input())
x=1
while x*(x+1)<n:
    x+=1
if x*(x+1)==n:
    print("YES")
else:
    print("NO")