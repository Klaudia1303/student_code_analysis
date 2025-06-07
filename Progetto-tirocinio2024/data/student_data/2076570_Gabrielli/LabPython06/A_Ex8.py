s1=input('inserisci stringa: ')
s2=input('inserisci stringa: ')
n=int(input('inserisci numero intero: '))

s3='' #devo trovare s3
for i in range(len(s1)):
    for j in range(1+i,len(s1)):
        if s1[1] in s2 and s1[j] in s2:
            if (s2.find(s1[1])>=i-n and s2.find(s1[i]<=i+n)and \
                s2.find(s1[j])>=j-n and s2.find(s1[j])<=j+n):
                   s3=s1[i]+s1[j]
print(s3)
