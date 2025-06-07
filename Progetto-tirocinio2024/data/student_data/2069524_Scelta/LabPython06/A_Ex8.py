s1=input('Inserisci una stringa non vuota:')
s2=input('Inserisci una stringa non vuota:')
n=int(input('Inserisci un numero intero:'))
risultato=''
for i in s1:
    for j in s2: 
        if i in s2 and(abs(s1.find(i)-s2.find(i)) <= n):
            risultato+=i
            break
print(risultato)
