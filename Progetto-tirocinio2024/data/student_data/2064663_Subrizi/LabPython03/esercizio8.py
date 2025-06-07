s = input('Inserisci una stringa palindroma: ')
s[0:]==s[::-1]
while s[0::]!=s[::-1]:
    s = input('non palindroma, inserisci una stringa palindroma: ')
print('stringa palindroma di lunghezza: ', len(s))
