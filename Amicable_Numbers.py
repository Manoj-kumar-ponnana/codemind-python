a=int(input())
b=int(input())
s1=s2=0
for i in range(1,a):
    if a%i==0:
        s1+=i
for i in range(1,b):
    if b%i==0:
        s2+=i
print("Amicable") if s1==b and s2==a else print("Not Amicable")