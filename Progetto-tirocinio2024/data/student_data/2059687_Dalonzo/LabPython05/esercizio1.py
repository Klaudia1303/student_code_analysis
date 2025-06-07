str1 = input('Inserire una stringa: ')
str2 = input('Inserire una stringa di lunghezza ' + str(len(str1)) + ' :')

for i in range(0,len(str1)):
    print(str1[i] + str2[i],end='')
