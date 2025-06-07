
stringa = "g3"
while(stringa.isalpha() == False or stringa.islower() == False):
    
    stringa = input('Inserire una stringa: ')
    print(stringa[0] + stringa[len(stringa) - 1])
    