s=input("Inserire una stringa: ")
m=0
for c in s:
    m=max(s.count(c),m)
    if m==int(s.count(c)):   s1=c
print("Carattere comparso più volte",s1)
