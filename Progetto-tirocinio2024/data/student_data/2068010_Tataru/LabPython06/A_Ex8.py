s1=input()
s2=input()
n=int(input())
sf=""
for i in s1:
    if (s2.find(i)!=-1):
        if(abs(s2.find(i)-s1.find(i))<=n):
            sf+=i
print(sf)
