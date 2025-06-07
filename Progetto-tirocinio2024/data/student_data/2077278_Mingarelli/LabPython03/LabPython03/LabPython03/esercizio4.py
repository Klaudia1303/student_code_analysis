n=int(input('inserisci il primo numero '))
m=int(input('insersci il secondo numero '))
z=0
if m>=0 and m<=10 and n>=0 and m<=10:
    while z<=10:
        if z==n or z==m:
            z+=1
        else:
            print(z)
            z+=1
else:
    print('uno dei 2 valori insieriti è sbagliato')
    
