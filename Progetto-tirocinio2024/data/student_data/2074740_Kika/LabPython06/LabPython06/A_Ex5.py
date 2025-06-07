s=input('inserisci stringa alfanumerica: ')
occ=1
k=2
c='a'
for i in range(1,len(s)):
    if  s[i]==s[i-1] :
        occ+=1
        c=s[i]
    if s[i]!=s[i-1] and occ>=k:
        k=occ
        occ=1
print(c,k)
