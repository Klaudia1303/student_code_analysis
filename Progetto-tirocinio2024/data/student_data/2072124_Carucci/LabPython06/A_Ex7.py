print('Inserire due stringhe non vuote :')
s1 = input(' - prima stringa: ')
s2 = input(' - seconda stringa: ')

s = ''
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        if s1[i:j] in s2:
            if len(s1[i:j]) >= len(s):
                s = s1[i:j]

        else:
            break
print(s)
