str1 = input('Inserire una stringa : ')
str2 = input('Inserire un\' altra stringa : ')
composta = ''
for i in range(0,len(str1)):
    if(str2.count(str1[i]) == 0):
        composta += str1[i]


print('La stringa composta di lettere nella prima stringa e non nella seconda : ' + composta)
