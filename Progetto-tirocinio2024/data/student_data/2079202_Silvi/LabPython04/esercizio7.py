l=""
r=0
s=input("inserire la stringa:")
for i in s:
    if l!=i:
        if r<s.count(i):
            r=s.count(i)
            l=i
print(l)
