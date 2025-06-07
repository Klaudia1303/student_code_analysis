s1=input('inserire una stringa: ')
s2=input('inserire una stringa: ')
n=int(input('inserire un numero intero: '))
l=''
i=0
c=0
for i in range(len(s1)):
    c=s1[i]
    if c in s2[max(0,i-n):min(len(s2),i+n)]:
        l+=c
print(l)
