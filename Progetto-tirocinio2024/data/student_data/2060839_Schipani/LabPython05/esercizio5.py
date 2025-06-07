s=input('inserire una stringa di almeno 2 caratteri: ')
n=int(input('inserire un numero positvo: '))
k=2
i=0
if len(s)>2 and k!=5:
    for i in range(len(s)-2):
        if s[i]==s[i+n]:
            print(True)
            k=5
    if k!=5:
        print(False)
