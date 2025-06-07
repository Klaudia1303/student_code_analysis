p=True
while p:
    s=str(input('Stringa palindroma '))
    if s == s[::-1]:
        print('Stringa palindroma di lunghezza '+str(len(s)))
        p=False
    else:
        print('Non palindroma, inserire una stringa palindroma ')
