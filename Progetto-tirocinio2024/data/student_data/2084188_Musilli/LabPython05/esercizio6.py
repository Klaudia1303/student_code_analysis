s=input("Inserire una stringa: ")
b=False
for c in s:
    s1=s[:s.find(c)]+s[s.find(c)+1:]
    for i in range(len(s1)):
        if s1[i]==c: b=True; break
    if b: break
if b:   i=s.rfind(c)-s.find(c)
else:   i=0
print("\nDistanza massima tra 2 caratteri uguali: ",i)
