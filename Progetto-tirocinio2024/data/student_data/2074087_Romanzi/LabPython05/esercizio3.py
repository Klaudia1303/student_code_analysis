s1=str(input('Stringa 1 '))
s2=str(input('Stringa 2 '))
for i in range(len(s1)):
    if s2.find(s1[i])== -1:
        print(s1[i],end='')
