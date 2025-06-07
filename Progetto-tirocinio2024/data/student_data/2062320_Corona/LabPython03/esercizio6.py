w= True

s= str(input())
i = 0
while w:
    if len(s)>0:
        print(s[i])
        i = i+1
        if len(s)==i:
            print('“stringa consumata e carattere non trovato”')
            w= False
        elif ord(s[i]) >= 100:
            print("Il primo carattere con codice Unicode maggiore di 100 è", s[i])
            w = False