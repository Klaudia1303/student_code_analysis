n_1=int(input('Inserisci il primo intero '))
n_2=int(input('Inserisci il secondo intero '))
i=1
prod=abs(n_1)
if(n_1==0 or n_2==0):
    print('0')
else:
    if (n_1>0 and n_2>0 or n_1 <0 and n_2<0):
        while i<abs(n_2):
            prod=prod+abs(n_1)
            i+=1
        print(abs(prod))
    elif (n_1<0 and n_2>0 or n_1>0 and n_2<0):
        while i<abs(n_2):
                prod=prod+abs(n_1)
                i+=1
        print(-prod)
