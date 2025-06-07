s=input('inserisci una stringa: ')
i=True

while i:
    s1=input('inserisci una stringa: ')
    if s[-1]==s1[0]:
        i=False
    else:
        s=s1

if not i:
    print(s,s1)
