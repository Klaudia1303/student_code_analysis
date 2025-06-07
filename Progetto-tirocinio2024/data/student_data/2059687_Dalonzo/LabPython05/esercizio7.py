stringa = input('Inserire una stringa : ')
check = False
for i in range(0, len(stringa)):
    if( stringa.count(stringa[i]) > 1):
        check = True


print(check)
