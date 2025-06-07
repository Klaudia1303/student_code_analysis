word=input('insert word: ')
scan=0
unicode=0
while unicode<=100:
    if scan==len(word):
        print('stringa consumata e carattere non trovato')
        quit()
    else:
        unicode=ord((word[scan:scan+1]))
        scan+=1
if unicode>100:
    print('Il primo carattere con codice Unicode maggiore di 100 è '+chr(unicode))
else:
    print('non trovato')