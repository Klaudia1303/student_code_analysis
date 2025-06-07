s1=input('inserire una stringa: ')
s2=input('inserire una seconda stringa: ')
for i in range(0,len(s1)):
    if s2.count(s1[i])==0:
        print(s1[i], end='')

