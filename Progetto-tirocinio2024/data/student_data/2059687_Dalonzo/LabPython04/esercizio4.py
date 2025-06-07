

num = -1
count = 0
while(int(num) != 0):
    num = input('Inserire un numero (0 per terminare): ')
    if(str(num) != '*'):
        if(int(num) % 3 == 0):
            count += 1
   


print('Numero Valori divisibili per 3 : ' + str(count))
