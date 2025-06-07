p=False
while not p :
    n=(input('inserisci una sringa palindroma: '))
    if n[-1]== n[0]:
        p = True
    else:
        print('non palindroma, inserire una stringa palindroma')
print('stringa palindroma di lunghezza ', len(n))
