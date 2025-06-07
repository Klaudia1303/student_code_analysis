uguali=False
sc=''
while not uguali:
    s=input('Inserire prima stringa: ')
    c=input('Inserire seconda stringa: ')
    if len(s)!=len(c):
        print('Le due stringhe non hanno la stessa lunghezza!')
    else:
        uguali=True
for i in range(len(s)):
    sc=sc+s[i]+c[i]
print('Stringa alternata:',sc)

