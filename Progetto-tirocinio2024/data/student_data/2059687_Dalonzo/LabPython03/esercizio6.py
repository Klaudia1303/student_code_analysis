

stringa = input('Inserire una stringa da almeno un carattere: ')

cont = 0
terminato = False
while(cont <= (len(stringa) - 1)):
    if(ord(stringa[cont]) > 100):
        print('Valore unicode del carattere : ' + str(ord(stringa[cont])) +  ', carattere  :' + stringa[cont] + " maggiore di 100")
        terminato = True
        break
    cont += 1
    

if(not terminato):
    print('Stringa consumata senza trovare il carattere')