s1=input('Inserire stringa s1: ')
while s1=='':
    s1=input ('Inserire di nuovo la stringa s1: ')
s2=input('Inserire stringa s2: ')
while s2=='':
    s2=input ('Inserire di nuovo la stringa s2: ')

n=int(input('Inserire numero n: '))
while n<=0:
    n=int(input ('Inserire di nuovo il numero n: '))
s=''
for i in range(len(s1)):
    f=s2.find(s1[i])
    if f==-1:
        continue
    

    if f-i<=n and i-f<=n:
        s=str(s)+str(s1[i])

print(s)
