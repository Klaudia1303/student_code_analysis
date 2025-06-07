n=input('inserisci una serie di stringhe, la sequenza verrà interrotta quando sarà immessa una stringa contenente sia il carattere ‘a’ che il carattere ‘c’: ')
if n=='':
    print('Non hai inserito nessuna stringa')
else:
    p=1
    f='c'
    l='a'
    while not f in (n) or not l in(n):
        n=input('inserisci una serie di stringhe, la sequenza verrà interrotta quando sarà immessa una stringa contenente sia il carattere ‘a’ che il carattere ‘c’: ')
        p=p+1
    print(p)
