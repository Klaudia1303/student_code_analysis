s=input('inserisci una stringa palindroma: ')
n=s[::-1]
if s==n :
    print('stringa palindroma di lunghezza ',len(s))
while s!=n:
    s=input('non palindroma, inserisci una stringa palindroma: ')
    n=s[::-1]
    if s==n:
        print('stringa palindroma di lunghezza ',len(s))
