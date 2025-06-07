s1=str(input('Inserisci stringa 1 '))
s2=str(input('Inserisci stringa 2 '))
precedente=''
for i in range(len(s1)):
    x=s1[i]
    if s2.count(x)<1:
        stringa=precedente+x
        precedente=stringa
print(stringa)
