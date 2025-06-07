s1=input('Inserire prima stringa: ')
s2=input('Inserire seconda stringa: ')
n=int(input('Inserire numero intero: '))
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] in s2:
            c=i
            z=s2.find(s1[i])
            if abs(c-z)<=n:
                print(s1[i],end='')
                break
            
