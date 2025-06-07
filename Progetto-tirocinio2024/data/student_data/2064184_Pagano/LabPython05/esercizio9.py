l = int(input("Inserisci un intero dispari >= 3: "))

print('*' * l)
for i in range(l-2):
    print('*' + ' '*(l-2) + '*')
print('*' * l)
