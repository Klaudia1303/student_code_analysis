s=input('Inserisci una stringa: ')
i=0
corretto=True
while i<len(s) and corretto:
    x=s.count(s[i])
    if x>=2:
        print(True)
        corretto=False
    i+=1
if x<2:
    print(False)