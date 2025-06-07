s1=input('inserisci stringa: ')
s2=input('inserisci stringa: ')
n=int(input('inserisci numero intero: '))
s3=''
for i in range (0,len(s1)):
    for j in range (i-n,i+n+1):
        if j>=0 and j<len(s2):
            if s1[i]==s2[j]:
                s3+=s1[i]

print(s3)
