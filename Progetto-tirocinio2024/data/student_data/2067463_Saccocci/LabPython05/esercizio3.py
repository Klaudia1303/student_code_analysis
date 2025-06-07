s1=input('Inserire una stringa:')
s2=input('Inserire una stringa:')
for i in s1:
    if i not in s2:
        print(i,end='')
