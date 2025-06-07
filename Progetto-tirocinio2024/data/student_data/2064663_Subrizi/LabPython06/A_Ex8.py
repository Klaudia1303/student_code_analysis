s1=input('Inserisci una stringa: ')
s2=input('Inserisci una stringa: ')
n=int(input('Inserisci un numero intero: '))
s=''
for i in range(0, len(s1)):
    if s1[i] in s2:
        for j in range(s2.find(s1[i]), len(s2)):
            if s1[i]==s2[j]:
                if abs(j-i)<=n:
                    s+=s1[i]
                    break
    else:
        continue
print(s)    

