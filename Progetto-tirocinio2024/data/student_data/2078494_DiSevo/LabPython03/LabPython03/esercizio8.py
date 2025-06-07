s = input('Inserisci una stringa palindroma: ')
while s[:] != s[::-1]:
    s = input('Errato, inserire una stringa palindroma: ')
if s[:] == s[::-1]:
    print('Stringa palindroma di lunghezza '+str(len(s)))
