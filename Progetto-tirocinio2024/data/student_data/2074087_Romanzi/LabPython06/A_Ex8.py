s1=str(input('Stringa 1 '))
s2=str(input('Stringa 2 '))
n=int(input('Intero '))
for i in range(len(s1)):
    if s2.find(s1[i])!=-1 and abs(s1.find(s1[i])-s2.find(s1[i]))<=n:
        print(s1[i],end='')
