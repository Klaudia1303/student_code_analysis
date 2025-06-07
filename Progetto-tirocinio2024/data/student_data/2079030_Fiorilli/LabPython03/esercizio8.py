s=input('inserisci una stringa palindroma: ')
while s[:]!=s[::-1]:
    s=input('non palindroma, inserisci una stringa palindroma: ')
print ('stringa palindroma di lunghezza ',len(s))
