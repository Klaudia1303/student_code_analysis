s1=input('inserisci una stringa:')
s2=input('inserisci una stringa della stessa lunghezza della precedente:')
finito=False
while not finito and len(s1)!=len(s2):
    s1=input('inserisci una stringa:')
    s2=input('inserisci una stringa della stessa lunghezza della precedente:')
    if len(s1)==len(s2):
        finito=True
        for  i in range(len(s1)):
            print(s1[i]+s2[i], end='')


