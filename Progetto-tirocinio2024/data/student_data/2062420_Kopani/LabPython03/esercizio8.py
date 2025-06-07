s=input('Inserire una parola palindorma: ')
while s[::1]!=s[::-1]:
    s=input('Inserire una parola palindroma: ')
print('Stringa palindroma di lunghezza',len(s))