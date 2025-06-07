

num = 0
somma = 0
while(num != '*'):
    num = input('Inserire un numero (* per terminare): ')
    if(str(num) != '*'):
        if(int(num) < 0):
            somma += int(num)
    num = str(num)


print('Somma valori negativi inseriti : ' + str(somma))
