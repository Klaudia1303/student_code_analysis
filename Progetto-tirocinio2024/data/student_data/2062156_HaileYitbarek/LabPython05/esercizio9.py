l=int(input('inserire intero dispari >=3 per il lato: '))
for i in range(0,l):
    if i==0 or i==l-1:
        print('*'*l)
    else:
        print('*'+' '*(l-2)+'*')
