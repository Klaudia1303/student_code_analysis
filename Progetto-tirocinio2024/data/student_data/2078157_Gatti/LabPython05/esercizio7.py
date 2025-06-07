s = input('inserisci una stringa: ')
c = 0
for i in s:
    if s.count(i) > 1:
        print('True')
        c += 1
        s = ''
if c == 0:
    print('False')
