n=list(input())
for i in range(len(n)):
    if n[i]=="6":
        n[i]="9"
        break
for j in n:
    print(j,end="")