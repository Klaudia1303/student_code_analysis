a=''
b=''
boo=True
while boo:
    s=input('inserisci una stringa: ')
    if len(s)==len(a)+len(b):
        boo=False
        print(a, b, s)
    a=b
    b=s
