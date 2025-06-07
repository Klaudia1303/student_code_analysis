s1=input('Inserire una stringa: ')
s2=input('Inserire una stringa: ')
for i in range(len(s1)):
    if s2.find(s1[i])==-1:
        print(s1[i], sep='', end='')