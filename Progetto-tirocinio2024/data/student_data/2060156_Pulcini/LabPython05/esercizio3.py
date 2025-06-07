s1=input('inserire una stringa:')
s2=input('inserire una stringa:')
for i in s1:
    if i not in s2:
        print(i,end='')
