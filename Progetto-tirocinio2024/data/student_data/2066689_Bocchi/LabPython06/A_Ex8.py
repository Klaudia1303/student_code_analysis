s1= input('stringa1: ')
s2= input('stringa2: ')
n= int(input('numero intero: '))
ris=''
for i in range(len(s1)):
    if s1[i] in s2:
        for j in range(len(s2)):
            if s2[j]==s1[i] and abs(j-i)<=n:
                ris+= s1[i]
                s2[j].replace(s2[j],'')
print(ris)
