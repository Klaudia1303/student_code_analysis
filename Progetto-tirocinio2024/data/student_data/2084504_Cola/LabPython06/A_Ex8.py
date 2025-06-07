s1=input('inserire una stringa: ')
s2=input('inserire una seconda stringa: ')
n=int(input('inserire un numero intero: '))
for i in range(0,len(s1)):
    x=s2.find(s1[i])
    if x==-1:
        continue
    elif i-x<=n and x-i<=n:
        print(str(s1[i]),end='')
    
