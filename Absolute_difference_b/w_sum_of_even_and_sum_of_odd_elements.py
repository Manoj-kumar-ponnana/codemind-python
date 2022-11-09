x=int(input())
l=list(map(int,input().split()))
os=es=0
for i in l:
    if i%2==0:
        es+=i
    else:
        os+=i
print(abs(es-os))