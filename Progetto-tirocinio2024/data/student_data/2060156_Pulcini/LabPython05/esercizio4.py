n1=int(input('inserire il primo intero:'))
n2=int(input('inserire il secondo intero:'))
if n1>0 and n2>0:
    for i in range(n1,n2):
        if i%n1==0:
            print(i)
else:
    print('errore')
