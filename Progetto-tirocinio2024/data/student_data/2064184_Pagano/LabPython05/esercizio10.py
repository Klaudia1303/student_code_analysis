l = int(input("Inserisci il lato di un quadrato: "))

print('*' * l)

for i in range(l-2):
    if i == 0:
        row = '*' + (' '*(l-4)) + '*'
    else:
        row = ' ' * (l-2)
        row = row[:i] + '*' + row[i+1:]
        row = row[:-i-1] + '*' + row[-i:]
    print('*'+row+'*')

print('*' * l)
