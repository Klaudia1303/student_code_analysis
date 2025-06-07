s = str(input('Insert string: '))
t = str(input('Insert string of the same lenght: '))
add = ''
if len(s)==len(t):
    for i in range(len(s)):
        add = add+(s[i]+t[i])
    print(add)
else:
    print('Strings of different lenght,restart program')
