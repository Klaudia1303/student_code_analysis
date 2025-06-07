s=input("inserire stringa: ")
c=0
j=0
i=0
while j<len(s)-1:
    if s.count(s[j])>=s.count(s[c]):
        c=j
        i=s[c]
    j+=1
print(s[c])
