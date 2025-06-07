

s=input("Inserire stringa:\t")

dist=0

for i in range(len(s)):
    a=s[i]
    if s.count(a) >= 2:
        r=s.rfind(a)
        
        dist=max(dist, (r-i))
print(dist)
