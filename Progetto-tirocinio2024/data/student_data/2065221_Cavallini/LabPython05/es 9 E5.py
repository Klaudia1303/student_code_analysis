b = int(input('inserisci una base: '))
s = ' '
for i in range(b):
    if i == 0 or i == b-1:
        print('*'*b)
    else:
        print('*',(s*(b-4)),'*')
print()
