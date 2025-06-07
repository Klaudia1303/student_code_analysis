s=input('Inserisci una stringa non vuota alfanumerica:')
max_occ=0
c=''
occ=0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        occ=0
    else:
        c=s[i]
        occ+=1
        max_occ=max(max_occ,occ+1)
        i+=1
print(c,max_occ)
