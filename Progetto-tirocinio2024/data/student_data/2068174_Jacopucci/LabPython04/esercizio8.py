c=0
s2=input('inserire una stringa: ')
while (s2==''):
    print('errore')
    s2=input('inserire una stringa: ')
s1=input('inserire una stringa: ')
while (s1==''):
    print('errore')
    s1=input('inserire una stringa: ')
while(c==1):
    if (s2[-1]==s1[1]):
        c+=1
    else:
        s2=s1
        s1=input('inserire una stringa: ')
print(s2+' '+s1)
    
