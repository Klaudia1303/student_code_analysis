s=str(input('Inserisci stringa 1 '))
t=str(input('Inserisci stringa 2 '))
precedente=''
if len(s)==len(t):
    for i in range(len(t)):
        x=s[i]
        y=t[i]
        stringanuova=y+x+precedente
        precedente=stringanuova
print(stringanuova[::-1])
