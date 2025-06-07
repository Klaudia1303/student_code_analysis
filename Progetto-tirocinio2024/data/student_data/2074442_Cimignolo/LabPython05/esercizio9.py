l=int(input('inserisci la misura del lato: '))

print('*'*l)
for i in range(1,l-1):
    print('*' + ' '*(l-2) + '*')
print('*'*l)
