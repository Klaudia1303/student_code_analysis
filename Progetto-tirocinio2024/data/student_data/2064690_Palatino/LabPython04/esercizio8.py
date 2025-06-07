s=input('inserisci una stringa non vuota: ')
t=input('inserisci una stringa non vuota: ')

while s[-1]!=t[0] or t[0]!=s[-1]:
    s=input('inserisci una stringa non vuota: ')
    t=input('inserisci una stringa non vuota: ')
    if s[-1]==t[0]:
        print(s,' ',t)
    elif t[0]==s[-1]:
        print(t,' ',s)
