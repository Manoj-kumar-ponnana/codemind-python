x=int(input())
l=list(map(int,input().split()))
os=es=0
for i in range(x):
    if i%2==0:
        es+=l[i]
    else:
        os+=l[i]
print(abs(es-os))