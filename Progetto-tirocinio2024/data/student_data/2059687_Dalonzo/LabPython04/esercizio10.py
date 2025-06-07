

stringa = ' '

totLen = 0
checked = False
index = 0

while(checked == False):

    stringa = input('Inserire una stringa: ')
    if(index == 0):
        primaS = stringa
    elif(index == 1):
        secondaS = stringa
    elif(index == 2):
        terzaS = stringa
        totLen = len(primaS) + len(secondaS)
        if(totLen == len(terzaS)):
            print(primaS + ' ' + secondaS + ' ' + terzaS)
            checked = True
    else:
        index = 0
        
    index += 1

    
