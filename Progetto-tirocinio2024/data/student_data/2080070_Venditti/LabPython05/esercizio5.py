s=input('inserire una stringa con almeno 2 caratteri: ')
n=int(input('inserire un intero: '))
i=0
x=True
while (i+n)<len(s):
    if s[i]==(s[i+n]) and x:
        print('True')
        x=False
    i+=1
if x==True:
    print('False')
