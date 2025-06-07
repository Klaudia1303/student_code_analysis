n=int(input('inserisci un numero '))
i=2
while n%i!=0:  #n.p. non devo avere resto fino a che non arrivo ad i==n
    i+=1
if i<n:
    print('non primo')
else:
        print('primo')
