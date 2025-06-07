s=input("Inserire la prima stringa:")
n=0
for i in range (len(s)):
    if(s.count(s[i])>=n):
        n=s.count(s[i])
        mag=s[i]
print(mag,n)
