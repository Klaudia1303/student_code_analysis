s1 = input('inserisci una stringa: ')
s2 = input('inserisci una stringa: ')
s3 = ''
n = int(input('inserisci una distanza: '))
for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        if s1[i] in s2 and s1[j] in s2:
            if (s2.find(s1[i]) >= i-n and s2.find(s1[i]) <= i+n and
                s2.find(s1[j]) >= j-n and s2.find(s1[j]) <= j+n):
                   s3 = s1[i]+s1[j]
print(s3)
