n=int(input('inserisci lato di un quadrato (dispari e >=3)'))
d=n-2
print (n*'*')
for j in range(d):
    print ('*', end='')
    print (' '*d, end='')
    print ('*')
print (n*'*')

