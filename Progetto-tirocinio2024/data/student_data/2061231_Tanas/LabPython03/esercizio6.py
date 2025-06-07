s = ''
while not len(s) > 0:
    s = input("stringa: ")

i = 0
while True:
    if i >= len(s):
        print('stringa consumata e carattere non trovato')
        break

    elif ord(s[i]) > 100:
        print('Il primo carattere con codice Unicode maggiore di 100 è', s[i])
        break

    i += 1
