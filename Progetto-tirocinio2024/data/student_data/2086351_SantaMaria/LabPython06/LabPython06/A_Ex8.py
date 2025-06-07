s1=input('Inserire una stringa: ')
s2=input('Inserire una stringa: ')
n=int(input('Inserire un numero intero: '))
for i in range(len(s1)):
    if s1[i] in s2[i-n:i+n+1]:
        print(s1[i],end='')
