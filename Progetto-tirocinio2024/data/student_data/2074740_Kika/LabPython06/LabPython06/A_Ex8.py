s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
n=int(input('inserisci un intero: '))
for i in range(len(s1)):
    for a in range(i-n,i+n+1):
        if 0<=a<len(s2) and s2[a]==s1[i]:
            print(s1[i], end='')
            break
            
