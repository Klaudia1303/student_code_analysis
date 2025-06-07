s=input("inserire una stringa: ")
r=0
maggiore=0
while r<len(s):
    conto=s.count(s[r])
    if conto>=maggiore:
        maggiore=conto
        t=s[r]
    r+=1
print(t)
