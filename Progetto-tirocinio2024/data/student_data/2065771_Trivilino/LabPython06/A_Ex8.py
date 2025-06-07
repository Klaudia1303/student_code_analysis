s1=input('Inserire una stringa: ')
s2=input('Inserire una seconda stringa: ')
n=int(input('Inserire un numero intero: '))
risultato=''
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if s1[i:i+1]==s2[j:j+1] and abs((s1.find(s1[i:i+1])-s2.find(s2[j:j+1])))<=n:
            #print('posizione1',s1.find(s1[i:i+1]),'posizione2',s2.find(s2[j:j+1]))
            risultato+=s1[i:i+1]
print(risultato)
