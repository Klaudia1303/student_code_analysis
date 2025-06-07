s1= input('Inserisci la prima stringa: ')
s2= input('Inserisci la seconda stringa: ')
s3 =''
for i in range (len(s1)):
    for j in range (len(s2)):
        if s1[i]==s2[j]:
            break
        else:
            if j==len(s2)-1:
                s3=s3+s1[i]
print (s3)
