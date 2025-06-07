print('Inserire due stringhe aventi la stessa lunghezza' )
s1 = input('- Prima stringa: ')
s2 = input('- Seconda stringa: ')

while len(s1)!=len(s2):
    print('\nLe stringhe devono avere la stessa lunghezza')
    s1 = input(' - Prima stringa: ')
    s2 = input(' - Seconda stringa: ')

for i in range(len(s1)):
    print(s1[i]+s2[i], end='')
