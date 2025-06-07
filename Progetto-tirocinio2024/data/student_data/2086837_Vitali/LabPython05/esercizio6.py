s=input("Inserisci stringa: ")
dmax=0
for i in range(len(s)):
    ind=s.rfind(s[i])
    if dmax<ind-i:
        dmax=ind-i
print(dmax)
