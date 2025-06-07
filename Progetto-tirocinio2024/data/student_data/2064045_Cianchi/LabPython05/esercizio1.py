s1=(input('inserisci una stringa:'))
s2=(input('inserisci una stringa della stessa lunghezza:'))
if len(s1)!=len(s2):
    s2=int(input('errato, inserisci una stringa della stessa lunghezza:'))
for i in range(len(s1)):
    print(s1[i],end='')
    print(s2[i],end='')
    
