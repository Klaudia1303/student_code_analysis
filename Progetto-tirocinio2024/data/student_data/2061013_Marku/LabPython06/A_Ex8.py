s1=input('inserire una stringa: ')
s2=input('inserire una stringa: ')
n=int(input('inserire un numero intero: '))

s=''
for i in range(len(s1)):
    f=s2.find(s1[i])
    if f==-1:
        continue
    
    if f-i<=n and i-f<=n:
        s=str(s)+str(s1[i])
        
print(s)
    
    
        
