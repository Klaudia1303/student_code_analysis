str1 = input('Inserire una stringa contenente almeno due caratteri : ')
num = int(input('Inserire un intero positivo : '))
check = False
for i in range(0,len(str1)):
    caratt = str1[i]
    if(i + num < len(str1)):
        if(caratt == str1[i + num]):
            check = True


print(check)
