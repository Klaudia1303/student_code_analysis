i = True
pre = ' '
while i:
    s = input('inserisci una stringa: ')
    if s[0] == pre[-1]: #primo carattere  di s = ultimo carattere di pre
        print(pre,s)
        i= False
    else:
        pre= s
        i = True
