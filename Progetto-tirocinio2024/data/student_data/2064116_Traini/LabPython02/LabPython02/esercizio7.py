n1=int(input('inserisci numero intero: '))
n2=int(input('inserisci input intero: '))
n3=int(input('inserisci input intero: '))
if n1>n2>n3:
    print('n1 \nn2 \nn3')
elif n2>n1>n3:
    print('n2 \nn1 \nn3')
elif n3>n2>n1:
    print('n3 \nn2 \nn1')
elif n2>n3>n1:
    print('n2 \nn3 \nn1')
elif n1>n3>2:
    print('n1 \nn3 \nn2')
elif n3>n1>n2:
    print('n3 \nn1 \nn2')
    
