s=input("Inserisci stringa alfanumerica: ")
c=s[0]
o=1
cmax=''
omax=0
for i in range(1,len(s)):
    if s[i]==c:
        o+=1
        if o>=omax:
            cmax=s[i]
            omax=o
    else:
        c=s[i]
        o=1
print(cmax,omax)
