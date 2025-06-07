l=0
while l<=0:
    l=int(input('inserisci il lato del quadrato: '))
for i in range(l):
    if i==0 or i==l-1:
        print ('*'*l)
    else:
        print ('*', end='')
        for j in range (1, l-1):
            if j==i or j==(l-1-i):
                print ('*', end='')
            else:
                print (' ', end='')
        print('*')
            
