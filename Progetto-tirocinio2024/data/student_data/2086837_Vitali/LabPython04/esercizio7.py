s=input("Inserisci stringa s: ")
l=len(s)
Max=0
for i in range(l):
    occ=s.count(s[i])
    if occ>=Max:
        Max=occ
        c=s[i]
print(c)

    
