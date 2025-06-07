print('Inserire due stringhe: ')
s1 = input('- Prima stringa: ')
s2 = input('- Seconda stringa: ')

for i in range(len(s1)):
    if s1[i] not in s2:
        print(s1[i], end='')
