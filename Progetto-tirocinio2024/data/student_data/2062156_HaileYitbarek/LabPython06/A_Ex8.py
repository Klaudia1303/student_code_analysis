s1=input('inserire stringa: ')
s2=input('inserire stringa: ')
n=int(input('inserire intero: '))
for i in range(len(s1)):
    if s1[i] in s2[i-n:i+n+1]:
        print(s1[i],end='')
