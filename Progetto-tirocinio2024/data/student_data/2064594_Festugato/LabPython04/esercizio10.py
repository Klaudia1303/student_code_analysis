i = True
adi1 = ''
adi2 = ''
while i:
    s = input('inserisci una stringa: ')
    if len(s) == len(adi1) + len(adi2):
        print(adi1,adi2,s)
        i= False
    else:
        adi1 = adi2
        adi2 = s
        i= True
    
