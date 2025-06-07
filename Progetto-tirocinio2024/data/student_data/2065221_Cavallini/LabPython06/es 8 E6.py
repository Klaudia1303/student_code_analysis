s1 = input('inserisci una stringa: ')
s2 = input('inserisci una stringa: ')
n = int(input('inserisci un numero: '))
s3 = ''
for i in range(len(s1)):
    c=s1[i]
    if c in s2:
        pos=s2.find(c)
        if i-n<=pos and pos<=i+n:
            s3=s3+c
print(s3)
