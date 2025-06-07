s1=input('inserisci una stringa:')
s2=input('inserisci una stringa:')
n=int(input('inserisci un numero intero:'))
for i in range(len(s1)):
    if s1[i] in s2:
        x=s1[i]
        y=s2.find(x)
        if abs(i-y)<=n:
            print(x,end='')
