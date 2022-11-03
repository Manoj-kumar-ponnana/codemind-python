lst=list(input())
c=0
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]==lst[j]:
            c+=1
if c==len(lst):
    print("Unique Number")
else:
    print("Not Unique Number")