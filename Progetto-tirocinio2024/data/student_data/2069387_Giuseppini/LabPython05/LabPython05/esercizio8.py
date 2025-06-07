b=int(input('inserisci un int dispari magg o uguale di 3: '))
for i in range(1,b+1,2):
    spazi=(b-i)//2
    print(' '*spazi+'*'*i)
