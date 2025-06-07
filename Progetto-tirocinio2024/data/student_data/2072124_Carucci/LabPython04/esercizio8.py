sp = ' '
s = input('Inserire una stringa non vuota: ')

while sp[-1]!=s[0]:
    sp = s
    s = input('Inserire una stringa non vuota: ')

print(sp, s)
