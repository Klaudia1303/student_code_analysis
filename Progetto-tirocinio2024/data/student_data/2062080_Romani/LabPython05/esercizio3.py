s1=input('Inserire stringa: ')
s2=input('Inserire stringa: ')
for i in s1:
    if s2.find(i)==-1:
        print(i,end='')
