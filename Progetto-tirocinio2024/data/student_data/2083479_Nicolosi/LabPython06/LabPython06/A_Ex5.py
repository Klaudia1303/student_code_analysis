s=input('Inserisci una stringa: ')
conta=0
for c in range(len(s)-1,0,-1):
    x=s.count(s[c])
    if x>1:
        conta=conta+x
        print(s[c],conta)
        break