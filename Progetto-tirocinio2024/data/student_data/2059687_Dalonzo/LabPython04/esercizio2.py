

num = 0
count = 0
while(num != '*'):
    num = input('Inserire un numero (* per terminare): ')
    if(str(num) != '*'):
        if(int(num) > 0):
            count += 1
    num = str(num)


print('Valori positivi inseriti : ' + str(count))
