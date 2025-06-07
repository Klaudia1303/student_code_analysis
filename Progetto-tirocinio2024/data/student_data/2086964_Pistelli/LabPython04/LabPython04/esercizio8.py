a=True
y=str(input('inserici una stringa '))
while a!=False:
    s=str(input('inserire una stringa '))
    if y[1]==s[0]:
        print(s,y)
        a=False
    y=str(input('inserire una stringa '))
    if s[1]==y[0]:
        print(y,s)
        a=False

