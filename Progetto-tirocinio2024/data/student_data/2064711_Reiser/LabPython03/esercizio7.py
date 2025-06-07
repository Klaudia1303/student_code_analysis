c= input('inserire un carattere: ')
t = True
while t==True:
    s= input('inserire una stringa: ')
    if s.count(c)>2:
        print('il numero di occorenze del carattere nella stringa è: '+str(s.count(c)))
        t= False
    else:
        ''
