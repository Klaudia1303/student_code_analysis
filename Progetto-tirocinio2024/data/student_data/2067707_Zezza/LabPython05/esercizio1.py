s1=input('stringa 1: ')
s2=input('stringa 2: ')
if len(s1)==len(s2):
    for i in range(len(s1)):
        print(s1[i]+s2[i],end='')
