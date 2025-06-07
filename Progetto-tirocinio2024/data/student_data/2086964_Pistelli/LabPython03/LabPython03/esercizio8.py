a=True
while a:
    s=str(input('scrivi una frase o parola '))
    if s[0: ]==s[::-1 ]:
        print("stringa palindroma di lunghezza " ,len(s))
        a=False
    else :
        print('non palindroma, inserire una stringa palindroma: ')
