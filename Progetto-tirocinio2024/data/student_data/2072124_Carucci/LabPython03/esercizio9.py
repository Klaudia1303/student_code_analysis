n = int(input('Inserire un numero intero: '))
primo = True
i = 2
while i<n and primo:
    if (n%i)!=0:
        i+=1
    else:
        primo = False
if primo:
    print('Numero  primo')
else:
    print('Numero non primo')
