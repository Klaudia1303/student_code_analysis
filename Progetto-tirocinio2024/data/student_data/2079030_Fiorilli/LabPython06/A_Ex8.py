s1=input('inserisci una stringa: ')
s2=input('inserisci un\'altra stringa: ')
n=int(input('inserisci un intero: '))
stringa=''
for i in range (len(s1)):
    if s1[i] in s2:
        for j in range (max((i-n),0),min((i+n), len(s2))):
            if s2[j]==s1[i]:
                stringa+=s1[i]
                break
print (stringa)
        
