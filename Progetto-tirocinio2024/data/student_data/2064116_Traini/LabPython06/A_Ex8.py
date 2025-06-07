s1=input('inserisci stringa: ')
s2=input('inserisci stringa: ')
n=int(input('inserisci intero: '))
c=''
a=''
for i in range(len(s1)):
    c=s1[i]
    for k in range(len(s1)):
        if s2.count(c,i-n,i+n)>0:
            a=a+c
            break
print(a)
