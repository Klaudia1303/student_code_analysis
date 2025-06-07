s=input('Inserisci una stringa: ')

i=0
while i==0:
    if s!=s[::-1]:
        s=input('Inserisci una stringa: ')
    else:
        print('Stringa palindroma di lunghezza ',len(s))
        i=1
