s1=input('inserisci la stringa: ')
s2=input('inserisci la stringa: ')
n=int(input('inserisci un intero: '))
s3=''
for i in range(len(s1)):
    for k in range(len(s2)):
        if s1[i]==s2[k] and abs(i-k)<=2:
            s3=s3+s1[i]
print(s3)
